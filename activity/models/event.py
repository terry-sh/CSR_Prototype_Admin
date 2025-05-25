from django.db import models
from .activity import Activity

# 活动中的事件
class Event(models.Model):
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="all_events",
        db_column="activity"
    )
    name = models.CharField('Name', max_length=256)
    description = models.TextField('Description')
