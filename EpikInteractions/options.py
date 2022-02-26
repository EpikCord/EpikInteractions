class BaseSlashCommandOption:
    def __init__(self, *, name: str, description: str, required: bool = False):
        self.name: str = name
        self.description: str = description
        self.required: bool = required
        self.type: int = None # Needs to be set by the subclass
        # People shouldn't use this class, this is just a base class for other options, but they can use this for other options we are yet to account for.

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "required": self.required,
            "type": self.type
        }

class Subcommand(BaseSlashCommandOption):
    def __init__(self, *, name: str, description: str, required: bool = False, options: list):
        super().__init__(name=name, description=description, required=required)
        self.type = 1
        self.options = options

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "required": self.required,
            "type": self.type,
            "options": [option.to_dict() for option in self.options]
        }


class SubCommandGroup(BaseSlashCommandOption):
    def __init__(self, *, name: str, description: str, required: bool = False):
        super().__init__(name=name, description=description, required=required)
        self.type = 2


class StringOption(BaseSlashCommandOption):
    def __init__(self, *, name: str, description: str, required: bool = False):
        super().__init__(name=name, description=description, required=required)
        self.type = 3


class IntegerOption(BaseSlashCommandOption):
    def __init__(self, *, name: str, description: str, required: bool = False):
        super().__init__(name=name, description=description, required=required)
        self.type = 4


class BooleanOption(BaseSlashCommandOption):
    def __init__(self, *, name: str, description: str, required: bool = False):
        super().__init__(name=name, description=description, required=required)
        self.type = 5


class UserOption(BaseSlashCommandOption):
    def __init__(self, *, name: str, description: str, required: bool = False):
        super().__init__(name=name, description=description, required=required)
        self.type = 6


class ChannelOption(BaseSlashCommandOption):
    def __init__(self, *, name: str, description: str, required: bool = False):
        super().__init__(name=name, description=description, required=required)
        self.type = 7


class RoleOption(BaseSlashCommandOption):
    def __init__(self, *, name: str, description: str, required: bool = False):
        super().__init__(name=name, description=description, required=required)
        self.type = 8


class MentionableOption(BaseSlashCommandOption):
    def __init__(self, *, name: str, description: str, required: bool = False):
        super().__init__(name=name, description=description, required=required)
        self.type = 9


class NumberOption(BaseSlashCommandOption):
    def __init__(self, *, name: str, description: str, required: bool = False):
        super().__init__(name=name, description=description, required=required)
        self.type = 10


class AttachmentOption(BaseSlashCommandOption):
    def __init__(self, *, name: str, description: str, required: bool = False):
        super().__init__(name=name, description=description, required=required)
        self.type = 11


class SlashCommandOptionChoice:
    def __init__(self, * name: str, value: float | int | str):
        self.name: str = name
        self.value: float | int | str = value
    
    def to_dict(self):
        return {
            "name": self.name,
            "value": self.value
        }