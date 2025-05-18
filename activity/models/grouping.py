from django.db import models
from .activity import Activity
from .language import Language

# 活动集合
# 将多个历史上的活动归类集合
# 例如：2025的种玉米活动，2026的种玉米活动
class ActivityGrouping(models.Model):
    # **可读性的ID**
    code = models.CharField('Code', max_length=256)

    # **名称**
    # 主要用于方便Admin用户管理活动
    name = models.CharField('Name', max_length=256)

    def __str__(self):
        return self.name

class ActivityGroupingTranslation(models.Model):
    grouping = models.ForeignKey(
        ActivityGrouping,
        on_delete=models.CASCADE,
        related_name="set",
        db_column="activity_grouping_translation__activity_grouping"
    )

    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name="set",
        db_column="activity_translation__language")

    # **集合名称**
    title = models.CharField('Title', max_length=256)

    # **集合简介**
    introduction = models.CharField('Introduction', max_length=256)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['activity_grouping', 'language'],
                name='unique_activity_grouping_translation__grouping__language'
            ),
        ]

class ActivityGroupingActivity(models.Model):
    grouping = models.ForeignKey(
        ActivityGrouping,
        on_delete=models.CASCADE,
        related_name="set",
        db_column="activity_grouping__activity_grouping"
    )
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="set",
        db_column="activity_grouping__activity"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['grouping', 'activity'],
                name='unique_activity_grouping_activity__grouping__activity'
            ),
        ]