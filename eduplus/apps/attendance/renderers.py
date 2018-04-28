from eduplus.apps.core.renderers import EduplusJSONRenderer


class AttendanceJSONRenderer(EduplusJSONRenderer):
    object_label = 'attendance'
    pagination_object_label = 'attendance'
    pagination_count_label = 'attendanceCount'