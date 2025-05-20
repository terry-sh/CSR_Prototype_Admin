from django.http import HttpResponse, HttpRequest
from django.db.models import Q

from rest_framework import viewsets

from ..models.language import Language
from ..models.activity import Activity, ActivityTranslation
from ..dto.activity import ActivityListItem
from ..serializer.activity import ActivityListItemSerializer

def create_activity_dto(activity: Activity, language: Language):
    tranlation = ActivityTranslation.objects.get(language=language, activity=activity)
    return ActivityListItem(
        id=activity.id,
        cover_image=activity.cover_image,
        start_date=activity.start_date,
        end_date=activity.end_date,
        name=tranlation.name,
        slogan=tranlation.slogan,
        location=tranlation.location,
        joined=False
    )

class ActivityListViewSet(viewsets.ViewSet):
    def list(self, request: HttpRequest):
        activity_type: str = request.GET.get('type', 'newest')
        language_code: str = request.GET.get('lang', 'zh-Hans-CN')

        query = Q(status=1) if activity_type == 'newest' else Q(status__in=[1, 2])
        raw_list = Activity.objects.filter(query)

        language: Language = Language.objects.get(code=language_code)
        activity_list: list[ActivityListItem] = [create_activity_dto(item, language) for item in raw_list]

        serializer = ActivityListItemSerializer(activity_list, many=True)
        return HttpResponse(serializer.data)