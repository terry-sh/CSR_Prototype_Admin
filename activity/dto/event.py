import datetime
import typing
from dataclasses import dataclass

@dataclass
class EventListItemDto:
    id: int
    name: str
    description: str
    activeIcon: str
    inactiveIcon: str
    canJoin: bool

@dataclass
class EventListDto:
    lang: str
    data: typing.List[EventListItemDto]
