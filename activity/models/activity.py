from django.db import models
from .language import Language

STATUS_CHOICE = (
    (0, 'Draft'),
    (1, 'Active'),
    (2, 'Deactive'),
)

# 活动
class Activity(models.Model):
    # **可读性的ID**
    # Example: csr_2025__corn_planting
    code = models.CharField('Code', max_length=256)

    # **名称**
    # 主要用于方便Admin用户管理活动
    name = models.CharField('Name', max_length=256)

    # **封面图片**
    # 用户app端的展示
    cover_image = models.ImageField('Covdr Image')

    # **开始时间**
    start_date = models.DateField('Start Date')

    # **结束时间**
    end_date = models.DateField('End Date')

    # **参加人数**
    # 用于限制活动参数的总人数
    capacity = models.IntegerField('Capacity')

    # **活动地点**
    location = models.CharField('Short Name', max_length=512)

    # **活动地点的地理数据**
    # 如：经度纬度行政区划信息。可用于地图的显示等
    geo_location = models.JSONField('Geo Location')

    # **活动状态**
    # 活动在Admin管理中的状态，用于上架下架隐藏等
    status = models.IntegerField(
        'Status',
        db_column = 'status',
        default=1,
        choices=STATUS_CHOICE)

    def __str__(self):
        return self.name

# 活动简介（翻译）
class ActivityTranslation(models.Model):
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="set",
        db_column="activity_translation__activity")

    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name="set",
        db_column="activity_translation__language")

    # 名称
    name = models.CharField('Name', max_length=256)
    # 简介
    introduction = models.TextField('Introduction')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['activity', 'language'],
                name='unique_activity_translation__activity__language'
            ),
        ]