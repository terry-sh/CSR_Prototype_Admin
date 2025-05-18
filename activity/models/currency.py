from django.db import models

class Currency(models.Model):
    code = models.CharField('Code', max_length=16)
    name = models.CharField('Name', max_length=128)
    symbol = models.CharField('Symbol', max_length=8)
