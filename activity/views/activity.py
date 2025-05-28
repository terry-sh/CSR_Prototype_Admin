import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpRequest
from django.db.models import Q
from django.contrib.auth.models import User

from rest_framework import viewsets

from ..models.language import Language
from ..models.activity import Activity, ActivityTranslation
from ..models.activity_enroll import ActivityEnroll

from ..dto.activity import ActivityListItemDto, ActivityListDto
from ..serializer.activity import ActivityListSerializer

def create_activity_item(activity: Activity, language: Language, user: User):
    # Content Translation
    tranlation = ActivityTranslation.objects.get(language=language, activity=activity)
    # Number of participants
    number_of_participants: int = ActivityEnroll.objects.filter(activity=activity, status=1).count()
    # Progress of activity, 0% - 100%
    progress: int = 10
    # Whether current use has joined the activity
    join_status: str = None
    if not user.is_anonymous:
        enroll_record = ActivityEnroll.objects.filter(user=user, activity=activity)
        if enroll_record.exists():
            approve_status = enroll_record[0].status
            join_status = 'Approved' if approve_status == 1 else 'Pending' if approve_status == 0 else 'Rejected'

    return ActivityListItemDto(
        id=activity.id,
        coverImage=activity.cover_image,
        startDate=activity.start_date,
        endDate=activity.end_date,
        name=tranlation.name,
        slogan=tranlation.slogan,
        location=tranlation.location,
        progress=progress,
        numberOfParticipants=number_of_participants,
        enrollStatus=join_status,
    )

class ActivityViewSet(viewsets.ViewSet):
    # Newest activities (In-Progress)
    def newest(self, request: HttpRequest):
        user = request.user
        language_code: str = request.GET.get('lang', 'zh-Hans-CN')

        language: Language = Language.objects.get(code=language_code)
        activity_list: list[ActivityListDto] = [create_activity_item(item, language, user)
          for item in Activity.objects.filter(status=1).order_by('-start_date')]

        list_dto = ActivityListDto(lang=language.code, data=activity_list)
        serializer = ActivityListSerializer(list_dto)
        json_content = json.dumps(serializer.data, ensure_ascii=False, cls=DjangoJSONEncoder)
        return HttpResponse(json_content, status=200, content_type="application/json")

    # All activities that are In-Progress or Done.
    # Return list with pagination.
    def all(self, request: HttpRequest):
        user = request.user
        language_code: str = request.GET.get('lang', 'zh-Hans-CN')

        language: Language = Language.objects.get(code=language_code)
        activity_list: list[ActivityListItemDto] = [create_activity_item(item, language, user)
          for item in Activity.objects.filter(status__in=[1, 2]).order_by('-start_date')]

        list_dto = ActivityListDto(lang=language.code, data=activity_list)
        serializer = ActivityListSerializer(list_dto)
        json_content = json.dumps(serializer.data, ensure_ascii=False, cls=DjangoJSONEncoder)
        return HttpResponse(json_content, status=200, content_type="application/json")

    # Fetch activity detail by ID
    def detail(self, request: HttpRequest, activity_id: int):
        user = request.user
        language_code: str = request.GET.get('lang', 'zh-Hans-CN')
        language: Language = Language.objects.get(code=language_code)

        activity_list: list[ActivityListItemDto] = [create_activity_item(item, language, user)
          for item in Activity.objects.filter(status__in=[1, 2]).order_by('-start_date')]

        list_dto = ActivityListDto(lang=language.code, data=activity_list)
        serializer = ActivityListSerializer(list_dto)
        json_content = json.dumps(serializer.data, ensure_ascii=False, cls=DjangoJSONEncoder)
        return HttpResponse(json_content, status=200, content_type="application/json")