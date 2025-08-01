from typing import Optional

class Node:
    def __init__(self, attendance):
        self.attendance = attendance  # Store full attendance object (e.g., a model instance)
        self.next: Optional['Node'] = None



class AttendanceLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_last(self):
        if not self.head:
            return None  # Linked list is empty

        if not self.head.next:
            last_node = self.head
            self.head = None
            return last_node

        prev = self.head
        current = self.head.next
        while current.next:
            prev = current
            current = current.next

        prev.next = None
        return current
attendance_linked_list= AttendanceLinkedList()
