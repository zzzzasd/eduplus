from rest_framework import status, viewsets
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Attendance
from .renderers import AttendanceJSONRenderer
from .serializers import (
    AttendanceSerializer
)

class AttendanceAPIView(APIView):
    serializer_class = AttendanceSerializer 
    permission_classes = (AllowAny,)
    renderer_classes = (AttendanceJSONRenderer,)

    from .models import Attendance
    queryset = Attendance.objects.all()
    
    def get_attendance(self, pk):
        try:
            return Attendance.objects.get(pk=pk)
        except AttendanceAPIView.DoesNotExist:
            raise ('404 not found')

    def get(self, request, *args, **kwargs):
        # There is nothing to validate or save here. Instead, we just want the
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        attendances = Attendance.objects.all()
        serializer = AttendanceSerializer(attendances, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

