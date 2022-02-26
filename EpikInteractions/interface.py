from quart import Quart, jsonify
from .command import Command

class Interface:
    """
    The class for registering commands
    """
    def __init__(self, *, public_application_key: str, endpoint_uri: str):
        self.endpoint_uri = endpoint_uri
        self.public_application_key = public_application_key
        self.commands: dict[str, Command] = {}
        quart_application = Quart(__name__)

        


    def command(self, *, name: str, description: str, guild_ids: list[str] = [], options = []):
        def register_slash_command(func):

            self.commands.append({
                "callback": func,
                "name": name,
                "description": description,
                "guild_ids": guild_ids,
                "options": options,
                "type": 1
            })
        return register_slash_command

    def user_command(self, *, name: str, description: str, guild_ids: list[str] = []):
        def register_slash_command(func):

            self.commands.append({
                "callback": func,
                "name": name,
                "description": description,
                "guild_ids": guild_ids,
                "type": 2
            })
        return register_slash_command

    def message_command(self, *, name: str, description: str, guild_ids: list[str] = []):
        def register_slash_command(func):

            self.commands.append({
                "callback": func,
                "name": name,
                "description": description,
                "guild_ids": guild_ids,
                "type": 3
            })
        return register_slash_command