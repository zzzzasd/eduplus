from django.contrib.auth.models import Group
from rest_framework import serializers

from eduplus.apps.authentication.serializers import UserSerializer

from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):

    users = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = ['daily_attendance', 'behavior', 'users']

    def create(self, validated_data):
        return Attendance(**validated_data)