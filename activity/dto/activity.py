import datetime
from dataclasses import dataclass
from rest_framework_dataclasses.serializers import DataclassSerializer

@dataclass
class ActivityListItem:
    id: int
    cover_image: str
    start_date: datetime.date
    end_date: datetime.date
    name: str
    slogan: str
    location: bool
    joined: bool
