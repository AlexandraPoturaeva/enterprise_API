from mptt.models import MPTTModel, TreeForeignKey
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Rule(TimeStampedModel):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'id {self.pk}: {self.title}'


class Position(TimeStampedModel):
    title = models.CharField(max_length=100, unique=True)
    rules = models.ManyToManyField(Rule, blank=True)

    def __str__(self):
        return f'id {self.pk}: {self.title}'


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


class Employee(TimeStampedModel):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth_date = models.DateField(max_length=50)
    division = models.ForeignKey(Division, models.PROTECT)
    positions = models.ManyToManyField(Position)

    class Meta:
        ordering = ['surname']
        unique_together = ['name', 'surname', 'birth_date']

    def __str__(self):
        return f'{self.name} {self.surname}'
