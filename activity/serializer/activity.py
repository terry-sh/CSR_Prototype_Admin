from rest_framework_dataclasses.serializers import DataclassSerializer
from ..dto.activity import ActivityListDto

class ActivityListSerializer(DataclassSerializer):
    class Meta:
        dataclass = ActivityListDto