from rest_framework_dataclasses.serializers import DataclassSerializer
from ..dto.activity import ActivityListItem

class ActivityListItemSerializer(DataclassSerializer):
    class Meta:
        dataclass = ActivityListItem