from django.db import models
from eduplus.apps.core.models import TimestampedModel


class Classroom(TimestampedModel):
    name = models.CharField(max_length=50, null=True)

    users = models.ManyToManyField('authentication.User')


    def __str__(self):
        return self.name