
# attendancedjango/views.py

from rest_framework import viewsets
from .models import Student, Classroom, AttendanceRecord
from .serializers import StudentSerializer, ClassroomSerializer, AttendanceRecordSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Classroom, AttendanceRecord
from .structures.linked_list import attendance_linked_list
from .structures.stack import attendance_stack
from .structures.graph import classroom_graph

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

class AttendanceRecordViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer


@api_view(['POST'])
def add_attendance(request):
    roll_no = request.data.get('roll_no')
    classroom_name = request.data.get('classroom')

    try:
        student = Student.objects.get(roll_no=roll_no)
        classroom = Classroom.objects.get(name=classroom_name)
        attendance = AttendanceRecord.objects.create(
          student=student,
          classroom=classroom
)
        attendance_dict = {
    'roll_no': student.roll_no,
    'name': student.name,
    'classroom': classroom.name,
    'timestamp': str(attendance.timestamp)
}

        attendance_linked_list.insert(attendance_dict)
        attendance_stack.push(attendance)

        return Response({'message': 'Attendance added successfully'}, status=status.HTTP_201_CREATED)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    except Classroom.DoesNotExist:
        return Response({'error': 'Classroom not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': f'Failed to add attendance: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def undo_last_attendance(request):
    try:
        last_node = attendance_linked_list.remove_last()
        if last_node:
            last_node.attendance.delete()
            return Response({'message': 'Last attendance record removed successfully'})
        else:
            return Response({'error': 'No attendance to undo'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': f'Failed to undo: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def connect_classrooms(request):
    room1 = request.data.get('room1')
    room2 = request.data.get('room2')

    try:
        c1 = Classroom.objects.get(name=room1)
        c2 = Classroom.objects.get(name=room2)
        c1.connected_rooms.add(c2)
        classroom_graph.add_edge(c1.name, c2.name)
        return Response({'message': 'Classrooms connected successfully'})
    except Classroom.DoesNotExist:
        return Response({'error': 'One or both classrooms not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def get_path(request):
    start = request.data.get('start')
    end = request.data.get('end')

    try:
        path = classroom_graph.bfs_path(start, end)
        if path:
            return Response({'path': path})
        else:
            return Response({'error': 'Path not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': f'Failed to find path: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    
