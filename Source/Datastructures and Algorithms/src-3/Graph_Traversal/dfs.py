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

    def depth_first_search(self, start=0):  # DFS implementation

        visited = set()
        visited.add(start)
        stack = [start]  # Stack should be a list, not a tuple
        dfs = []

        while stack:
            current = stack.pop()  # LIFO: Last in, First out
            dfs.append(current)
            for neighbour in self.graph[current]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)  # Push unvisited neighbors onto the stack
        return dfs


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

    print("DFS Traversal:", g.depth_first_search())
