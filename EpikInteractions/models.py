from typing import (
    TypeVar,
    Type
)
from datetime import datetime
from pydantic import BaseModel

CT = TypeVar('CT', bound='Colour')


class Colour:
    # Some of this code is sourced from discord.py, rest assured all the colors are different from discord.py
    __slots__ = ('value',)

    def __init__(self, value: int):
        if not isinstance(value, int):
            raise TypeError(
                f'Expected int parameter, received {value.__class__.__name__} instead.')

        self.value: int = value

    def _get_byte(self, byte: int) -> int:
        return (self.value >> (8 * byte)) & 0xff

    def __eq__(self, other) -> bool:
        return isinstance(other, Colour) and self.value == other.value

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return f'#{self.value:0>6x}'

    def __int__(self) -> int:
        return self.value

    def __repr__(self) -> str:
        return f'<Colour value={self.value}>'

    def __hash__(self) -> int:
        return hash(self.value)

    @property
    def r(self) -> int:
        """Return the red component in rgb"""
        return self._get_byte(2)

    @property
    def g(self) -> int:
        """Return the green component in rgb"""
        return self._get_byte(1)

    @property
    def b(self) -> int:
        """Return the blue component in rgb"""
        return self._get_byte(0)

    def to_rgb(self) -> tuple[int, int, int]:
        """Returns an rgb color as a tuple"""
        return (self.r, self.g, self.b)

    @classmethod
    def from_rgb(cls: Type[CT], r: int, g: int, b: int) -> CT:
        """Constructs a :class:`Colour` from an RGB tuple."""
        return cls((r << 16) + (g << 8) + b)

    @classmethod
    def lime_green(cls: Type[CT]) -> CT:
        """Returns a color of lime green"""
        return cls(0x00ff01)

    @classmethod
    def light_green(cls: Type[CT]) -> CT:
        """Returns a color of light green"""
        return cls(0x00ff22)

    @classmethod
    def dark_green(cls: Type[CT]) -> CT:
        """Returns a color of dark green"""
        return cls(0x00570a)

    @classmethod
    def light_blue(cls: Type[CT]) -> CT:
        """Returns a color of light blue"""
        return cls(0x00ff01)

    @classmethod
    def dark_blue(cls: Type[CT]) -> CT:
        """Returns a color of dark blue"""
        return cls(0x0a134b)

    @classmethod
    def light_red(cls: Type[CT]) -> CT:
        """Returns a color of light red"""
        return cls(0xaa5b54)

    @classmethod
    def dark_red(cls: Type[CT]) -> CT:
        """Returns a color of dark red"""
        return cls(0x4c0000)

    @classmethod
    def black(cls: Type[CT]) -> CT:
        """Returns a color of black"""
        return cls(0x000000)

    @classmethod
    def white(cls: Type[CT]) -> CT:
        """Returns a color of white"""
        return cls(0xffffff)

    @classmethod
    def lightmode(cls: Type[CT]) -> CT:
        """Returns the color of the background when the color theme in Discord is set to light mode. An alias of `white`"""
        return cls(0xffffff)

    @classmethod
    def darkmode(cls: Type[CT]) -> CT:
        """Returns the color of the background when the color theme in Discord is set to dark mode"""
        return cls(0x363940)

    @classmethod
    def amoled(cls: Type[CT]) -> CT:
        """Returns the color of the background when the color theme in Discord is set to amoled mode. An alias of `black`"""
        return cls(0x000000)

    @classmethod
    def blurple_old(cls: Type[CT]) -> CT:
        """Returns the old Discord Blurple color"""
        return cls(0x7289da)

    @classmethod
    def blurple_new(cls: Type[CT]) -> CT:
        """Returns the new Discord Blurple color"""
        return cls(0x5865f2)

    default = black

Color = Colour

class Embed:  # Always wanted to make this class :D
    def __init__(self, *,
                 title: str | None = None,
                 description: str| None = None,
                 color: Colour| None = None,
                 video: dict| None = None,
                 timestamp: datetime| None = None,
                 colour: Colour | None = None,
                 url: str| None = None,
                 type: int| None = None,
                 footer: dict| None = None,
                 image: dict| None = None,
                 thumbnail: dict| None = None,
                 provider: dict| None = None,
                 author: dict| None = None,
                 fields: list[dict] | None = None,
                 ):
        self.type: int = type
        self.title: str| None = title
        self.type: str| None = type
        self.description: str| None = description
        self.url: str| None = url
        self.video: dict| None = video
        self.timestamp: str| None = timestamp
        self.color: Colour| None = color or colour
        self.footer: str| None = footer
        self.image: str| None = image
        self.thumbnail: str| None = thumbnail
        self.provider: str| None = provider
        self.author: dict| None = author
        self.fields: list[str] | None= fields

    def add_field(self, *, name: str, value: str, inline: bool = False):
        self.fields.append({"name": name, "value": value, "inline": inline})

    def set_thumbnail(self, *, url: str| None = None, proxy_url: str| None = None, height: int| None = None, width: int| None = None):
        config = {
            "url": url
        }
        if proxy_url:
            config["proxy_url"] = proxy_url
        if height:
            config["height"] = height
        if width:
            config["width"] = width

        self.thumbnail = config

    def set_video(self, *, url: str| None = None, proxy_url: str| None = None, height: int| None = None, width: int| None = None):
        config = {
            "url": url
        }
        if proxy_url:
            config["proxy_url"] = proxy_url
        if height:
            config["height"] = height
        if width:
            config["width"] = width

        self.video = config

    def set_image(self, *, url: str| None = None, proxy_url: str| None = None, height: int| None = None, width: int| None = None):
        config = {
            "url": url
        }
        if proxy_url:
            config["proxy_url"] = proxy_url
        if height:
            config["height"] = height
        if width:
            config["width"] = width

        self.image = config

    def set_provider(self, *, name: str| None = None, url: str| None = None):
        config = {}
        if url:
            config["url"] = url
        if name:
            config["name"] = name
        self.provider = config

    def set_footer(self, *, text: str| None, icon_url: str| None = None, proxy_icon_url: str| None = None):
        payload = {}
        if text:
            payload["text"] = text
        if icon_url:
            payload["icon_url"] = icon_url
        if proxy_icon_url:
            payload["proxy_icon_url"] = proxy_icon_url
        self.footer = payload

    def set_author(self, name: str| None = None, url: str| None = None, icon_url: str| None = None, proxy_icon_url: str| None = None):
        payload = {}
        if name:
            payload["name"] = name
        if url:
            payload["url"] = url
        if icon_url:
            payload["icon_url"] = icon_url
        if proxy_icon_url:
            payload["proxy_icon_url"] = proxy_icon_url

        self.author = payload

    def set_fields(self, *, fields: list[dict]):
        self.fields = fields

    def set_color(self, *, colour: Colour):
        self.color = colour.value

    def set_timestamp(self, *, timestamp: datetime.datetime):
        self.timestamp = timestamp.isoformat()

    def set_title(self, title: str| None = None):
        self.title = title

    def set_description(self, description: str| None = None):
        self.description = description

    def set_url(self, url: str| None = None):
        self.url = url

    def to_dict(self):
        final_product = {}

        if getattr(self, "title"):
            final_product["title"] = self.title
        if getattr(self, "description"):
            final_product["description"] = self.description
        if getattr(self, "url"):
            final_product["url"] = self.url
        if getattr(self, "timestamp"):
            final_product["timestamp"] = self.timestamp
        if getattr(self, "color"):
            final_product["color"] = self.color
        if getattr(self, "footer"):
            final_product["footer"] = self.footer
        if getattr(self, "image"):
            final_product["image"] = self.image
        if getattr(self, "thumbnail"):
            final_product["thumbnail"] = self.thumbnail
        if getattr(self, "video"):
            final_product["video"] = self.video
        if getattr(self, "provider"):
            final_product["provider"] = self.provider
        if getattr(self, "author"):
            final_product["author"] = self.author
        if getattr(self, "fields"):
            final_product["fields"] = self.fields

        return final_product

class Attachment:
    def __init__(self, data: dict):
        self.id: str = data["id"]
        self.filename: str = data["filename"]
        self.description: str | None = data.get("description")
        self.content_type: str | None = data.get("content_type")
        self.size: int = data["size"]
        self.url: str = data["url"]
        self.proxy_url: str = data["proxy_url"]
        self.height: int | None = data.get("height")
        self.width: int | None = data.get("width")
        self.ephemeral: bool | None = data.get("ephemeral")

class ChannelMention:
    def __init__(self, data: dict):
        self.id: str = data["id"]
        self.guild_id: str = data["guild_id"]
        self.type: int = data["type"]
        self.name: str = data["name"]

class User:
    def __init__(self, data: dict):
        self.id: int = data["id"]
        self.username: str = data["username"]
        self.discriminator: str = data["discriminator"]
        self.avatar: str = data["avatar"]
        self.bot: bool | None = data.get("bot")
        self.mfa_enabled: bool | None = data.get("mfa_enabled")
        self.accent_color: int | None = data.get("accent_color")
        self.locale: str | None = data.get("locale")
        self.verified: bool | None = data.get("verified")
        self.email: str | None = data.get("email")
        self.flags: int | None = data.get("flags")
        self.premium_type: int | None = data.get("premium_type")
        self.public_flags: int | None = data.get("public_flags")

class GuildMember:
    def __init__(self, data):
        self.user: User | None = data.get("user")
        self.nick: str | None = data.get("nick")
        self.avatar: str | None = data.get("avatar")
        self.roles: list[str] = data["roles"]
        self.joined_at: str = data["joined_at"]
        self.premium_since: str | None = data.get("premium_since")
        self.deaf: bool = data["deaf"]
        self.mute: bool = data["mute"]
        self.pending: bool | None = data.get("pending")
        self.permissions: str | None = data.get("permissions")
        self.communication_disabled_until: str | None = data.get("communication_disabled_until")

class PartialGuildMember(User):
    ...

class Emoji:
    def __init__(self, data: dict):
        self.id: str = data["id"]
        self.name: str = data["name"]
        self.user: User | None = User(data.get("user")) if data.get("user") else None
        self.roles: list[str] | None = data.get("roles")
        self.require_colons: bool | None = data.get("require_colons")
        self.managed: bool | None = data.get("managed")
        self.animated: bool | None = data.get("animated")
        self.available: bool | None = data.get("available")

class Reaction:
    def __init__(self, data: dict):
        self.count: int = data["count"]
        self.me: bool = data["me"]
        self.emoji: Emoji = data["emoji"]

class Message:
    def __init__(self, data):
        self.id: str
        self.channel_id: str
        self.guild_id: str
        self.author: User | None
        self.member: PartialGuildMember | None
        self.content: str | None
        self.timestamp: str
        self.edited_timestamp: str | None
        self.tts: bool
        self.mention_everyone: bool
        self.mentions: list[User]
        self.mention_roles: list[str]
        self.mention_channels: list[ChannelMention]
        self.attachments: list[Attachment]
        self.embeds: list[Embed]
        self.reactions: list[Reaction]

class Interaction(BaseModel):
    """
    An interaction from JSON to a Python Class
    """
    id: str
    application_id: str
    type: int
    data: dict
    guild_id: str | None
    channel_id: str | None
    member: GuildMember | None
    user: User
    token: str
    version: int
    message: Message
    locale: str | None
    guild_locale: str | None