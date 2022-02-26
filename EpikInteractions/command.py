class Command:
    def __init__(self, *, name: str, description: str, options: list[dict], callback: callable):
        self.name = name
        self.description = description
        self.options = options
        self.callback = callback