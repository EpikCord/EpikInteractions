class Attachment:
    """
    Represents an Attachment on Discord

    Do not manually construct this class.

    Attributes:
    -----------
        id
            The attachment's Id
        filename
            The name of the file attached.
        description
            The description set for the file
        content_type
            The attachement's media type (Not related to Discord)
        size
            The size of the file in bytes
        url
            The source URL of the file
        proxy_url
            A proxied URL of the file
        height
            The height of the file if it's an image
        width
            The width of the file if it's an image
        ephemeral
            If the attachment is ephemeral
    """
    def __init__(self, data: dict):
        self.id: str = data.get("id")
        self.filename: str = data.get("filename")
        self.description: str = data.get("description")
        self.content_type: str = data.get("content_type")
        self.size: int = data.get("size")
        self.url: str = data.get("url")
        self.proxy_url: str = data.get("proxy_url")
        self.height: int = data.get("height")
        self.width: int = data.get("width")
        self.ephemeral: bool = data.get("ephemeral")