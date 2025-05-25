from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpRequest

from rest_framework import viewsets

from ..models.activity import Activity
from ..models.activity_enroll import ActivityEnroll

class ActivityEnrollViewSet(viewsets.ViewSet):
    # Enroll activity
    def enroll(self, request: HttpRequest, activity_id: int):
        result: bool = False
        user = request.user
        activity = Activity.objects.get(pk=activity_id)
        is_enrolled = ActivityEnroll.objects.filter(activity=activity, user=user).exists()
        if not is_enrolled:
            enroll = ActivityEnroll.objects.create(activity=activity, user=user)
            enroll.save()
        return HttpResponse(result, status=200, content_type="application/json")