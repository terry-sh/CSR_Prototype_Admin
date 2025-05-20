import datetime
import typing
from dataclasses import dataclass

@dataclass
class ActivityListItem:
    id: int
    cover_image: str
    start_date: datetime.date
    end_date: datetime.date
    name: str
    slogan: str
    location: str
    joined: bool

@dataclass
class ActivityList:
    lang: str
    data: typing.List[ActivityListItem]
