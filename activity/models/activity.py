from django.db import models
from .language import Language

ACTIVITY_STATUS_CHOICE = (
    (0, 'Draft'),
    (1, 'Active'),
    (2, 'Finished'),
    (3, 'Discard'),
)

# 活动
class Activity(models.Model):
    # **Code**，可读性的ID
    # Example: csr_2025__corn_planting
    code = models.CharField('Code', max_length=256)

    # **名称**
    # 主要用于方便Admin用户管理活动
    name = models.CharField('Name', max_length=256)

    # **封面图片/ICON**
    # 用户app端的展示
    cover_image = models.ImageField('Cover Image')

    # **开始时间**
    start_date = models.DateTimeField('Start Date')

    # **结束时间**
    end_date = models.DateTimeField('End Date')

    # **报名开始时间**，可选
    enroll_start_date = models.DateTimeField('Enroll Start Date', null=True)

    # **报名终止时间**，可选
    enroll_end_date = models.DateTimeField('Enroll End Date', null=True)

    # **参加人数**
    # 用于限制活动参数的总人数
    capacity = models.IntegerField('Capacity', default=500)

    # **活动地点的地理数据**
    # 如：经度纬度行政区划信息。可用于地图的显示等
    geo_location = models.JSONField('Geo Location', null=True)

    # **活动状态**
    # 活动在Admin管理中的状态，用于上架下架隐藏等
    status = models.IntegerField(
        'Status',
        db_column = 'status',
        default=1,
        choices=ACTIVITY_STATUS_CHOICE)

    def __str__(self):
        return self.name

# 活动简介（翻译）
class ActivityTranslation(models.Model):
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="translations",
        db_column="activity")

    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name="activity_translations",
        db_column="language")

    # 名称
    name = models.CharField('Name', max_length=256)

    # 简短的口号
    slogan = models.CharField('Slogan', max_length=256)

    # **活动地点**
    location = models.CharField('Location', max_length=512)

    # 简介
    introduction = models.TextField('Introduction', default='')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['activity', 'language'],
                name='unique_activity_translation__activity__language'
            ),
        ]