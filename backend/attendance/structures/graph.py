from collections import deque, defaultdict

class ClassroomGraph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, room1, room2):
        if room2 not in self.adjacency_list[room1]:
            self.adjacency_list[room1].append(room2)
        if room1 not in self.adjacency_list[room2]:
            self.adjacency_list[room2].append(room1)

    def bfs_path(self, start, end):
        if start not in self.adjacency_list or end not in self.adjacency_list:
            return []

        visited = set()
        queue = deque([[start]])

        while queue:
            path = queue.popleft()
            room = path[-1]
            if room == end:
                return path
            if room not in visited:
                visited.add(room)
                for neighbor in self.adjacency_list[room]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

        return []


classroom_graph = ClassroomGraph()
