class AttendanceStack:
    def __init__(self):
        self.stack = []

    def push(self, attendance):
        self.stack.append(attendance)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Singleton instance
attendance_stack = AttendanceStack()
