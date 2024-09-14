from collections import deque

class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)

    def print_graph(self):
        for u in self.graph:
            print(u, "->", self.graph[u])

    def breadth_first_search(self, start=0):  # Corrected method name
        queue = deque([start])
        visited = set()
        visited.add(start)
        bfs = []
        while queue:
            print(queue)  # Optional: debugging line to show queue status
            current = queue.popleft()
            bfs.append(current)
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return bfs

if __name__ == "__main__":

    g = Graph()

    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,2)
    g.add_edge(2,4)
    g.add_edge(2,3)
    g.add_edge(4,3)
    g.add_edge(4,5)
    g.add_edge(2,1)

    g.print_graph()

    print("BFS Traversal:", g.breadth_first_search())
