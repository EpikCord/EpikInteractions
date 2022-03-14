from .channels import VoiceChannel
from datetime import datetime
from typing import Optional
from .user import User

class RoleTag:
    def __init__(self, data: dict):
        self.bot_id: Optional[str] = data.get("bot_id")
        self.integration_id: Optional[str] = data.get("integration_id")
        self.premium_subscriber: Optional[bool] = data.get(
            "premium_subscriber")


class Role:
    def __init__(self, client, data: dict):
        self.data = data
        self.client = client
        self.id: str = data.get("id")
        self.name: str = data.get("name")
        self.color: int = data.get("color")
        self.hoist: bool = data.get("hoist")
        self.icon: Optional[str] = data.get("icon")
        self.unicode_emoji: Optional[str] = data.get("unicode_emoji")
        self.position: int = data.get("position")
        self.permissions: str = data.get("permissions")  # TODO: Permissions
        self.managed: bool = data.get("managed")
        self.mentionable: bool = data.get("mentionable")
        self.tags: RoleTag = RoleTag(self.data.get("tags"))

class Member:
    def __init__(self, http, data: dict):
        self.raw_data: dict = data
        self.id: int = data["id"]
        self.user: User = User(http, data["user"])
        self.nick: str | None = data.get("nick")
        self.roles: list[Role] = [Role(http, role) for role in data["roles"]]
        self.joined_at: datetime = datetime.strptime(data["joined_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        self.premium_since: datetime | None = None
        if "premium_since" in data:
            self.premium_since = datetime.strptime(data["premium_since"], "%Y-%m-%dT%H:%M:%S.%fZ")
        self.mute: bool = data["mute"]
        self.deaf: bool = data["deaf"]
        self.self_mute: bool = data["self_mute"]
        self.self_deaf: bool = data["self_deaf"]
        self.joined_voice_channel: VoiceChannel | None = None
        if "joined_voice_channel" in data:
            self.joined_voice_channel = VoiceChannel(http, data["joined_voice_channel"])
        self.voice_channel_id: str | None = data.get("voice_channel_id")
        self.voice_session_id: str | None = data.get("voice_session_id")
        self.voice_channel_id: str | None = data.get("voice_channel_id")
        self.self_stream: bool = data["self_stream"]
        self.self_video: bool = data["self_video"]
        self.afk: bool = data["afk"]
        self.system: bool = data["system"]
        self.suppress_everyone: bool = data["suppress_everyone"]
        self.mute: bool = data["mute"]
        self.deaf: bool = data["deaf"]