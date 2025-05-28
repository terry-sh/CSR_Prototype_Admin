import datetime
import typing
from dataclasses import dataclass

@dataclass
class ActivityListItemDto:
    id: int
    coverImage: str
    startDate: datetime.datetime
    endDate: datetime.datetime
    name: str
    slogan: str
    location: str
    progress: int
    numberOfParticipants: int
    enrollStatus: typing.Optional[str]

@dataclass
class ActivityListDto:
    lang: str
    data: typing.List[ActivityListItemDto]
