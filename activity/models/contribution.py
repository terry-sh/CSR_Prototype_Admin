from django.db import models
from .language import Language
from .unit import Unit
from .event import ActivityEvent

# 活动中可贡献的项目
class ContributionItem(models.Model):
    event = models.ForeignKey(
        ActivityEvent,
        on_delete=models.CASCADE,
        related_name="all_contributions",
        db_column="event")

    name = models.CharField('Name', max_length=256)

    # 贡献的默认值
    defaultValuue = models.DecimalField('Default Value', default=1)

    # 用户是否允许自定义贡献值
    customizable = models.BooleanField('Is Customizable')

    # 贡献的最小值
    mininumValue = models.DecimalField('Minumum Value', null=True)

    # 贡献的最大值
    maximumValue = models.DecimalField('Maximum Value', null=True)

    # 贡献的单位，比如：
    # - 次数：参加了X次
    # - 距离：跑了X米
    # - 天数：坚持了X天
    # - 金额：贡献了X元
    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name="related_contributions",
        db_column="unit")

class ContributionTranslation(models.Model):
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name="contribution_translations",
        db_column="language")
    contribution_item = models.ForeignKey(
        ContributionItem,
        on_delete=models.CASCADE,
        related_name="all_translations",
        db_column="contribution_item")
    name = models.CharField('Name', max_length=256)
    description = models.TextField('Description')

# 用户贡献值
class UserContribution(models.Model):
    contribution = ContributionItem
    # 贡献值
    value = models.DecimalField('Value')
    # 扩展信息（备用）
    extension = models.CharField('Extension')