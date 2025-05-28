from django.db import models
from .language import Language

# 单位
# 比如：时间（年，月，天，时，分，秒），长度（米），重量（千克），金额，分数，次数，等级
class Unit(models.Model):
    # 可读的短名
    name = models.CharField('Name', max_length=256)

    # 通用简写，如 y，m，d，h，km，kg等
    abbr = models.CharField('Code', max_length=64, default='')

# 单位（翻译）
class UnitTranslation(models.Model):
    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name="translations")

    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name="unit_translations")

    # 某个语言中的名称
    name = models.CharField('Name', max_length=256)

    # 格式化模板
    format_template = models.TextField('Format Template', null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['unit', 'language'],
                name='unique_unit_translation__unit__language'
            ),
        ]