from django.db import models
from .activity import Activity
from .language import Language

# 活动分类
class Category(models.Model):
    name = models.CharField('Name', max_length=256)
    description = models.TextField('Description')

class CategoryTranslation(models.Model):
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name="category_translations",
        db_column="catetory_translation__language")

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="translations",
        db_column="catetory_translation__category")

    name = models.CharField('Name', max_length=256)

    description = models.TextField('Description')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['language', 'category'],
                name='unique_category_translation__language__category'
            ),
        ]

class CategoryActivity(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="all_activities",
        db_column="catetory_activity__category")

    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
        related_name="category",
        db_column="catetory_activity__activity")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['category', 'activity'],
                name='unique_category_activity__category__activity'
            ),
        ]