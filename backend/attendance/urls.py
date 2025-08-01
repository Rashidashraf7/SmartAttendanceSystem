from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, ClassroomViewSet, AttendanceRecordViewSet
from . import views

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'attendance', AttendanceRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add-attendance/', views.add_attendance),
    path('undo-attendance/', views.undo_last_attendance),
    path('connect-classrooms/', views.connect_classrooms),
    path('get-path/', views.get_path),
]
