from rest_framework import serializers
from .models import Student, Classroom, AttendanceRecord

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    connected_rooms = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Classroom.objects.all()
    )

    class Meta:
        model = Classroom
        fields = ['id', 'name', 'connected_rooms']

class AttendanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = '__all__'
