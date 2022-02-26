from .command import Command

class Interface:
    """
    The class for registering commands
    """
    def __init__(self, public_application_key):
        self.public_application_key = public_application_key
        self.commands: dict[str, Command] = {}
    
    def command(self, *, name: str, description: str, options: list[dict]):
        def register_command(func):
            self.commands[name] = Command(name=name, description=description, options=options, callback=func)
        return register_command