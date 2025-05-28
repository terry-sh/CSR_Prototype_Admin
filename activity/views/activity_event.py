import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User

from rest_framework import viewsets

from ..models.language import Language
from ..models.activity import Activity
from ..models.event import ActivityEvent, ActivityEventTranslation
from ..dto.event import EventListItemDto, EventListDto
from ..serializer.event import EventListSerializer

def create_event_item(event: ActivityEvent, language: Language, user: User):
    # Content Translation
    tranlation = ActivityEventTranslation.objects.get(language=language, event=event)
    canJoin: bool = False
    if not user.is_anonymous:
        # TODO
        canJoin = True

    return EventListItemDto(
        id=event.id,
        name=tranlation.name,
        activeIcon=event.active_icon,
        inactiveIcon=event.inactive_icon,
        description=tranlation.description,
        canJoin=canJoin
    )

class ActivityEventViewSet(viewsets.ViewSet):
    # Enroll activity
    def all_events(self, request: HttpRequest, activity_id: int):
        user = request.user
        activity = Activity.objects.get(pk=activity_id)
        language_code: str = request.GET.get('lang', 'zh-Hans-CN')
        language: Language = Language.objects.get(code=language_code)

        event_list: list[EventListItemDto] = [create_event_item(item, language, user)
          for item in ActivityEvent.objects.filter(activity=activity)]

        list_dto = EventListDto(lang=language.code, data=event_list)
        serializer = EventListSerializer(list_dto)
        json_content = json.dumps(serializer.data, ensure_ascii=False, cls=DjangoJSONEncoder)
        return HttpResponse(json_content, status=200, content_type="application/json")