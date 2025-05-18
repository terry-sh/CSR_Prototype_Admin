from django.db import models
from .enum import STATUS_CHOICE

class Language(models.Model):
    # 语言代码
    # 如：zh-Hans-CN，en-US，en-SG 等
    code = models.CharField('Language Code', max_length=63)

    # 该语言的本地名称，例如：
    # 中国的中文：简体中文
    # 英文：English
    native_name = models.CharField('Native Name', max_length=127)

    # 排序
    sort = models.IntegerField(
        'Sorting Order',
        db_column = 'order',
        default=1,
    )

    status = models.IntegerField(
        'Show Status',
        db_column = 'status',
        default=1,
        choices=STATUS_CHOICE,
    )

    def __str__(self):
        return self.native_name
