from django.db import models
from .activity import Activity
from .language import Language

# 活动中的可参与事件
class ActivityEvent(models.Model):
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="all_events",
        db_column="activity"
    )
    name = models.CharField('Name', max_length=256)

    # 用户可参与的最大次数
    maximum_times = models.IntegerField('Maximum Times', default=1)

    # 用户未参与时的图标
    inactive_icon = models.ImageField('Cover Image')

    # 用户已参与时的图标
    active_icon = models.ImageField('Cover Image')

class ActivityEventTranslation(models.Model):
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name="event_translations",
        db_column="language")
    event = models.ForeignKey(
        ActivityEvent,
        on_delete=models.CASCADE,
        related_name="all_translations",
        db_column="event")
    name = models.CharField('Name', max_length=256)
    description = models.TextField('Description', default='')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['event', 'language'],
                name='unique_event_translation__event__language'
            ),
        ]