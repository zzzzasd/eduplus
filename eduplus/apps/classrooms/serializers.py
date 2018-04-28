from rest_framework import serializers

from eduplus.apps.authentication.serializers import UserSerializer

from .models import Classroom

class ClassroomSerializer(serializers.ModelSerializer):
    student_name = serializers.StringRelatedField(source='apps.authentication.User.name', many=True)
    class Meta:
        model = Classroom
        fields = ['name','student_name']
