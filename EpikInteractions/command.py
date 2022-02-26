class Command:
    def __init__(self, *, name: str, description: str, options: list[dict[str, dict[str, str]]], callback: callable):
        self.name = name
        self.description = description
        self.options = options
        self.callback = callback

class OptionChoice:
    def __init__(self, *, name: str, value: str | int | float):
        self.name = name
        self.value = value
    
    def to_dict(self):
        return {
            "name": self.name,
            "value": self.value
        }

class InvalidCommandOption(Exception):
    ...

class StringCommandOption:
    def __init__(self, *, name: str, description: str, required: bool = False, choices: list[OptionChoice] = [], auto_complete: bool = False):
        self.name = name
        self.description = description
        self.required = required
        self.type = 3
        self.choices = choices if choices else None
        if choices and auto_complete:
            raise InvalidCommandOption("You cannot set auto_complete to True if you have choices set.")
        
        

    
    def to_dict(self):
        payload = {
            "name": self.name,
            "description": self.description,
            "required": self.required,
            "type": self.type
        }

        if self.choices:
            payload["choices"] = self.choices
        
        return payload

class IntegerCommandOption(StringCommandOption):
    def __init__(self, *, name: str, description: str, required: bool = False, choices: list[OptionChoice] = []):
        super().__init__(name=name, description=description, required=required, choices = choices)
        self.type = 4
        self.






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