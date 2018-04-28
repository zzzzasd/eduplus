from django.db import models
from eduplus.apps.core.models import TimestampedModel


class Attendance(TimestampedModel):
    ATTENDANCE_OUTCOME = (
        ('PRE', 'Present'),
        ('LAT', 'Late'),
        ('ABS', 'Absent'),
    )
    BEHAVIOR_OUTCOME = (
        ('NOR', 'Normal'),
        ('PRO', 'Problematic'),
    )
    daily_attendance = models.CharField(max_length=3, choices=ATTENDANCE_OUTCOME, default='PRE')
    behavior = models.CharField(max_length=3, choices=BEHAVIOR_OUTCOME, default='NOR')

    users = models.ManyToManyField(
        'authentication.User',
        related_name='attendees'
    )

    def __str__(self):
        return str(self.created_at)

    def attend(self, user):
        self.users.add(user)

    def absent(self, user):
        self.users.remove(user)

    def is_attending(self, user):
        return self.users.filter(pk=user.pk).exists()