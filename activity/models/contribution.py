from django.db import models
from enum import CONTRIBUTION_UNIT
from .event import Event

# 活动中可贡献的项目
class Contribution(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="set",
        db_column="event")

    # 贡献的最小值
    mininum = models.DecimalField('Minumum')

    # 贡献的最大值
    maximum = models.DecimalField('Maximum')

    # 贡献的单位，比如：
    # - 次数：参加了X次
    # - 距离：跑了X米
    # - 天数：坚持了X天
    # - 金额：贡献了X元
    unit = models.CharField('Unit', choices=CONTRIBUTION_UNIT)

class ContributionTranslation(models.Model):
    name = models.CharField('Name', max_length=256)
    description = models.TextField('Description')

# 用户贡献值
class UserContribution(models.Model):
    contribution = Contribution
    # 贡献值
    value = models.DecimalField('Value')
    # 单位的扩展。比如金额的货币币种等。
    unitExtension= models.CharField('Unit Extension')