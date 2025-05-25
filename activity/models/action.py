from django.db import models
from .activity import Activity

class Action(models.Model):
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="activity_actions",
        db_column="activity"
    )
    name = models.CharField('Name', max_length=256)
    description = models.TextField('Description')
