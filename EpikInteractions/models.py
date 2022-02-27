from pydantic import BaseModel

class Interaction(BaseModel):
    """
    JSON Body for interactions
    """
    id: str
    application_id: str
    type: int
    data: dict
    guild_id: str | None
    channel_id: str | None
    member: dict | None
    user: dict | None
    token: str
    version: int
    message: dict| None
    locale: str | None
    guild_locale: str | None