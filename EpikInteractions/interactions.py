from .member import GuildMember

class BaseInteraction:
    def __init__(self, http,  data: dict):
        self.raw_data: dict = data
        self.id: int = data["id"]
        self.application_id: str = data["application_id"]
        self.type: int = data["type"]
        self.interaction_data: dict | None = data.get("interaction_data")
        self.guild_id: str | None = data.get("guild_id")
        self.channel_id: str | None = data.get("channel_id")
        self.member: GuildMember | None = GuildMember(http, data.get("member"))
        self.client