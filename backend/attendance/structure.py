from __future__ import annotations  # 👈 allows self-referencing type hints

class AttendanceNode:
    def __init__(self, data):
        self.data = data
        self.next_node: AttendanceNode | None = None  # 👈 renamed

class AttendanceLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = AttendanceNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:  # 👈 updated here
                current = current.next_node
            current.next_node = new_node  # 👈 updated here

    def to_list(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next_node  # 👈 updated here
        return result

class AttendanceStack:
    def __init__(self):
        self.stack = []

    def push(self, record):
        self.stack.append(record)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    
class ClassroomGraph:
    def __init__(self):
        self.graph = {}

    def add_classroom(self, room_name):
        if room_name not in self.graph:
            self.graph[room_name] = []

    def add_connection(self, room1, room2):
        self.graph.setdefault(room1, []).append(room2)
        self.graph.setdefault(room2, []).append(room1)

    def get_connections(self, room_name):
        return self.graph.get(room_name, [])

    def bfs_path(self, start, end):
        from collections import deque
        visited = set()
        queue = deque([[start]])

        while queue:
            path = queue.popleft()
            room = path[-1]

            if room == end:
                return path

            if room not in visited:
                visited.add(room)
                for neighbor in self.graph.get(room, []):
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        return None

