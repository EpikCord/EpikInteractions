from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from .interactions import *
from aiohttp import ClientSession
from quart import request, Response
from typing import (
    Union,
    List,
    Optional
)
from .commands import SlashCommand, UserCommand, MessageCommand, AnyOption        

def interaction_from_type(data: dict):
    if data["type"] == 1:
        return PingInteraction(data)
    elif data["type"] == 2:
        return ApplicationCommandInteraction(data)
    elif data["type"] == 3:
        return MessageComponentInteraction(data)
    elif data["type"] == 4:
        return AutoCompleteInteraction(data)
    elif data["type"] == 5:
        return ModalSubmitInteraction(data)

class HTTPClient:
    def __init__(self, *args, **kwargs):
        self.session = ClientSession(*args, **kwargs)
        self.base_uri = "https://discord.com/api/v9"
        

    async def get(self, url, *args, **kwargs):
        if url.startswith("/"):
            url = url[1:]
        return await self.session.get(f"{self.base_uri}/{url}", *args, **kwargs)

    async def post(self, url, *args, **kwargs):
        if url.startswith("/"):
            url[1:]
        return await self.session.post(f"{self.base_uri}/{url}", *args, **kwargs)
    
    async def put(self, url, *args, **kwargs):
        if url.startswith("/"):
            url[1:]
        return await self.session.put(f"{self.base_uri}/{url}", *args, **kwargs)
    
    async def delete(self, url, *args, **kwargs):
        if url.startswith("/"):
            url[1:]
        return await self.session.delete(f"{self.base_uri}/{url}", *args, **kwargs)

    async def patch(self, url, *args, **kwargs):
        if url.startswith("/"):
            url[1:]
        return await self.session.patch(f"{self.base_uri}/{url}", *args, **kwargs)

    async def close(self):
        await self.session.close()

class Interface:
    """
    The class that you are going to be using to work with Interactions. This is probably the only class you'll need to see and use.

    Attributes:
    -----------
    key: str The public API key you got from the developer portal. This is safe to share according to Discord Developers server.
    http: HTTPClient The HTTPClient object that is used to make requests.
    commands: List[Union[SlashCommand, UserCommand, MessageCommand]] The list of commands that you have created.
    synced_commands: bool Whether or not the sync_commands method has been called to sync commands with Discord.

    Methods:
    --------
    `async`:meth:`process_commands(request)` - Request class from Quart.

    Decorators:
    -----------
    :meth:`command(*, name: str, description: str, guild_ids: Optional[List[str]], options: Optional[List[Union[Subcommand, SubCommandGroup, StringOption, IntegerOption, BooleanOption, UserOption, ChannelOption, RoleOption, MentionableOption, NumberOption]]])` - Makes a function a Slash Command.

    :meth:`user_command(*, name: str)` - Makes a User Command.

    :meth:`message_command(*, name: str)` - Makes a Message Command.

    *async*:meth:`sync_commands()` - Syncs the commands that you have created with Discord. This will overwrite all existing commands on Discord.
    """
    def __init__(self, *, public_key: str):
        self.key: str = public_key
        self.commands: List[Union[SlashCommand, UserCommand, MessageCommand]] = []
        self._synced_commands: bool = False
        self.session: HTTPClient = HTTPClient()
    
    def command(self, *, name: str, description: str, guild_ids: Optional[List[str]] = [], options: Optional[AnyOption] = []):
        def register_slash_command(func):
            self.commands.append(SlashCommand(**{
                "callback": func,
                "name": name,
                "description": description,
                "guild_ids": guild_ids,
                "options": options,
                "type": 1
            })) # Cheat method.
        return register_slash_command

    def user_command(self, *, name: str):
        def register_slash_command(func):
            self.commands.append(UserCommand(**{
                "callback": func,
                "name": name,
            }))
        return register_slash_command

    def message_command(self, *, name: str):
        def register_slash_command(func):

            self.commands.append(MessageCommand(**{
                "callback": func,
                "name": name,
            }))
        return register_slash_command

    def synced_commands(self):
        return self._synced_commands

    async def sync_commands(self):
        """
        Syncs the commands that you have created with Discord. This will overwrite all existing commands on Discord.
        """
        command_sorter = {
            "global": []
        }

        async def bulk_overwrite_global_application_commands(commands: List[Union[SlashCommand, UserCommand, MessageCommand]]):
            payload = [command.to_discord_command_dict() for command in commands]
            await self.http.put(f"/applications/{self.id}/commands", json =  payload)

        async def bulk_overwrite_guild_application_commands(guild_id: str, commands: List[SlashCommand]):
            payload = [command.to_discord_command_dict() for command in commands]
            await self.http.put(f"/applications/{self.id}/guilds/{guild_id}/commands", json =  payload)

        for command in self.commands:
            command_payload = {
                "name": command["name"],
                "type": command["type"]
            }

            if command["type"] == 1:
                command_payload["description"] = command["description"]
                command_payload["options"] = [option.to_dict() for option in command["options"]]

            if command.get("guild_id"):
                if command_sorter.get(command["guild_id"]):
                    command_sorter[command["guild_id"]].append(command_payload)
                else:
                    command_sorter[command["guild_id"]] = [command_payload]
            else:
                command_sorter["global"].append(command_payload)

        for guild_id, commands in command_sorter.items():

            if guild_id == "global":
                await bulk_overwrite_global_application_commands(commands)
            else:
                await bulk_overwrite_guild_application_commands(guild_id, commands)
        
        self._synced_commands = True

    async def process_commands(self):
        """
        Process commands on this endpoint.
        """
        interaction_data = await request.get_data().decode("utf-8")

        verify_key = VerifyKey(bytes.fromhex(self.key))

        signature = request.headers["X-Signature-Ed25519"]
        timestamp = request.headers["X-Signature-Timestamp"]
        try:
            verify_key.verify(f'{timestamp}{interaction_data}'.encode(), bytes.fromhex(signature))
        except BadSignatureError:
            return Response(status = 401)
        interaction = interaction_from_type(interaction_data)

        if interaction.is_ping():
            return jsonify({
                "type": 1
            })

        if interaction.is_application_command():
            command = self.commands.get(interaction.command_name)
            if command:
                await command.callback(interaction)