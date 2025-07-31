from django.contrib import admin
from .models import Student, Classroom, AttendanceRecord

admin.site.register(Student)
admin.site.register(Classroom)
admin.site.register(AttendanceRecord)

