class Interface:
    """
    The class that you are going to be using to work with Interactions. This is probably the only class you'll need to see and use.

    Attributes:
    -----------
    key: str The public API key you got from the developer portal. This is safe to share according to Discord Developers server.
    @command: 
    """
    def __init__(self, *, public_key: str):
        self.key: str = public_key