from rest_framework_dataclasses.serializers import DataclassSerializer
from ..dto.event import EventListDto

class EventListSerializer(DataclassSerializer):
    class Meta:
        dataclass = EventListDto