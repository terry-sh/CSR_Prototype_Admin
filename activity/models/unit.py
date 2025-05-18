from django.db import models

'''
CONTRIBUTION_UNIT = (
    ('d', 'Days'),
    ('h', 'Hours'),
    ('y', 'Years'),
    ('m', 'Months'),
    ('km', 'Kilometers'),
    ('kg', 'Kilograms'),
    ('S', 'Scores'),
    ('G', 'Grade'),
    ('T', 'Times'),
)
'''

# 单位
# 比如：时间（年，月，天，时，分，秒），长度（米），重量（千克），金额，分数，次数，等级
class Unit(models.Model):
    # 可读的短名
    short_name = models.CharField('Short Name', max_length=256)
    # 代号，如 y，m，d，h，km，kg等
    code = models.CharField('Code', max_length=64)

# 单位（翻译）
class UnitTranslation(models.Model):
    # 名称
    name = models.CharField('Name', max_length=256)
    # 简介
    introduction = models.TextField('Introduction')