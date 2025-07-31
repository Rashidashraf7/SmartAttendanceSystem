from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    face_encoding = models.BinaryField(blank=True, null=True)  # Used later with OpenCV
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.roll_no} - {self.name}"


class Classroom(models.Model):
    name = models.CharField(max_length=100)
    connected_rooms = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.name


class AttendanceRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.classroom.name if self.classroom else 'N/A'} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"



