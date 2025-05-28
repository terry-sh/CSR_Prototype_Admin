import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpRequest
from django.db.models import Q
from django.contrib.auth.models import User

from rest_framework import viewsets

from ..models.language import Language
from ..models.activity import Activity, ActivityTranslation
from ..models.activity_enroll import ActivityEnroll

from ..dto.activity import ActivityListItem, ActivityList
from ..serializer.activity import ActivityListSerializer

def create_activity_item(activity: Activity, language: Language, user: User):
    # Content Translation
    tranlation = ActivityTranslation.objects.get(language=language, activity=activity)
    # Number of participants
    number_of_participants: int = ActivityEnroll.objects.filter(activity=activity, approved=True).count()
    # Progress of activity, 0% - 100%
    progress: int = 10
    # Whether current use has joined the activity
    approve_status: str = None
    if not user.is_anonymous:
        enroll_record = ActivityEnroll.objects.filter(user=user, activity=activity)
        if enroll_record.exists():
            approve_status = enroll_record[0].status

    return ActivityListItem(
        id=activity.id,
        coverImage=activity.cover_image,
        startDate=activity.start_date,
        endDate=activity.end_date,
        name=tranlation.name,
        slogan=tranlation.slogan,
        location=tranlation.location,
        progress=progress,
        numberOfParticipants=number_of_participants,
        enrollStatus=approve_status,
    )

class UserViewSet(viewsets.ViewSet):
    def detail(self, request: HttpRequest):
        user = request.user
        #language_code: str = request.GET.get('lang', 'zh-Hans-CN')
        #language: Language = Language.objects.get(code=language_code)

        activity_list: list[ActivityListItem] = [create_activity_item(item, language, user)
          for item in Activity.objects.filter(status__in=[1, 2]).order_by('-start_date')]

        list_dto = ActivityList(lang=language.code, data=activity_list)
        serializer = ActivityListSerializer(list_dto)
        json_content = json.dumps(serializer.data, ensure_ascii=False, cls=DjangoJSONEncoder)
        return HttpResponse(json_content, status=200, content_type="application/json")