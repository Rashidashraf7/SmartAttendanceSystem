from django.contrib import admin
from .models import Student, Classroom, AttendanceRecord




@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name', 'joined_on')
    search_fields = ('roll_no', 'name')

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('connected_rooms',)

@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'classroom', 'timestamp')
    list_filter = ('classroom', 'timestamp')


