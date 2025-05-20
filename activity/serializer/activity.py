from rest_framework_dataclasses.serializers import DataclassSerializer
from ..dto.activity import ActivityListItem, ActivityList

class ActivityListSerializer(DataclassSerializer):
    class Meta:
        dataclass = ActivityList