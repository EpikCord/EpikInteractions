from .role import Role
from .attachment import Attachment
from .message import Message
from .channels import channel_from_type
from quart import jsonify
from .user import User
from .member import GuildMember

class BaseInteraction:
    def __init__(self, http, data: dict, headers: dict):
        self.raw_data: dict = data
        self.id: int = data["id"]
        self.headers: dict = headers
        self.application_id: str = data["application_id"]
        self.type: int = data["type"]
        self.interaction_data: dict | None = data.get("interaction_data")
        self.guild_id: str | None = data.get("guild_id")
        self.channel_id: str | None = data.get("channel_id")
        self.member: GuildMember | None = GuildMember(http, data.get("member"))
        self.user: User | None = User(http, data.get("user")) if data.get("user") else None
        self.token: str = data["token"]
        self.version: int = data["version"]
        self.message: Message | None = Message(http, data.get("message")) if data.get("message") else None
        self.locale: str | None = data.get("locale")
        self.guild_locale: str | None = data.get("guild_locale")

    def is_ping(self):
        return self.type == 1
    
    def is_application_command(self):
        return self.type == 2
    
    def is_message_component(self):
        return self.type == 3
    
    def is_autocomplete(self):
        return self.type == 4
    
    def is_modal_submit(self):
        return self.type == 5

class PingInteraction(BaseInteraction):
    async def reply(self):
        return jsonify({
            "type": 1
        })

class ResolvedDataManager:
    def __init__(self, http, data: dict):
        self.data: dict
        self.http = http
        self.users: list[User] | None = [User(http, user) for user in data.get("users", [])] if data.get("users") else None
        self.members: list[GuildMember] | None = [GuildMember(http, member) for member in data.get("members", [])] if data.get("members") else None
        self.roles: list[Role] | None = [Role(http, role) for role in data.get("roles", [])] if data.get("roles") else None
        self.channels = [channel_from_type(http, channel) for channel in data.get("channels", [])] if data.get("channels") else None
        self.messages: list[Message] | None = [Message(http, message) for message in data.get("messages", [])] if data.get("messages") else None
        self.attachments: list[Attachment] | None = [Attachment(attachment) for attachment in data.get("attachments", [])] if data.get("attachments") else None

class ApplicationCommandInteraction(BaseInteraction):
    def __init__(self, http, data: dict, headers: dict):
        super().__init__(http, data, headers)
        self.command_name: str = self.data["command_name"]
        self.command_id: str = self.data["command_id"]
        self.command_type: int = data["type"]
        self.resolved: ResolvedDataManager = ResolvedDataManager(http, self.data.get("resolved"))
        self._options: dict = self.data.get("options")
    
    async def reply()