class Command:
    def __init__(self, *, name: str, description: str, options: list[dict[str, dict[str, str]]], callback: callable):
        self.name = name
        self.description = description
        self.options = options
        self.callback = callback

class ApplicationCommand:
    def __init__(self, data: dict):
        self.command_id: str = data["id"]
        self.command_type: int = data.get("type", 1)
        self.application_id: str | None = data.get("application_id")
        self.guild_id: str = data.get("guild_id")
        self.command_name: str = data["name"]
        self.description: str = data["description"]
        self.default_permission: bool = data.get("default_permission", True)
        self.version: str = data["version"]

class SlashCommand(ApplicationCommand):
    def __init__(self, data: dict):
        super().__init__(data)