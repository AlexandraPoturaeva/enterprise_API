from mptt.models import MPTTModel, TreeForeignKey
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Division(MPTTModel, TimeStampedModel):
    title = models.CharField(max_length=100)
    parent_division = TreeForeignKey(
        'self',
        models.CASCADE,
        null=True,
        blank=True,
        related_name='children_division',
    )

    class MPTTMeta:
        order_insertion_by = ['title']
        parent_attr = 'parent_division'

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title
