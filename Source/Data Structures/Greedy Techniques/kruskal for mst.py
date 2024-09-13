class DisjointSet:
    def __init__(self, n):
        # Initialize parent and rank arrays for n elements
        self.parent = list(range(n))  # Each node is its own parent initially
        self.rank = [0] * n  # Rank is used to keep the tree flat

    def find(self, u):
        # Find the representative (root) of the set containing u
        # Path compression is applied here to make future operations faster
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Recursively find the root and compress the path
        return self.parent[u]

    def union(self, u, v):
        # Union by rank: attach the smaller tree under the root of the larger tree
        root_u = self.find(u)  # Find the root of set containing u
        root_v = self.find(v)  # Find the root of set containing v

        if root_u != root_v:
            # Attach the tree with smaller rank under the tree with larger rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u  # Attach root_v to root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v  # Attach root_u to root_v
            else:
                # If ranks are the same, arbitrarily attach one tree to the other and increase rank
                self.parent[root_v] = root_u
                self.rank[root_u] += 1  # Increase the rank of root_u

def kruskal(n, edges):
    """
    Kruskal's algorithm to find the Minimum Spanning Tree (MST).

    :param n: Number of vertices
    :param edges: List of edges in the format (u, v, weight)
    :return: A tuple containing the MST as a list of edges and the total weight of the MST
    """
    # Initialize Disjoint Set for union-find operations
    ds = DisjointSet(n)

    # Step 1: Sort the edges by their weights
    # Time complexity: O(E log E), where E is the number of edges
    edges.sort(key=lambda x: x[2])

    mst = []  # To store the edges of the MST
    total_weight = 0  # To store the total weight of the MST

    # Step 2: Iterate over sorted edges and add to MST if it doesn't form a cycle
    # Time complexity: O(E log V), where E is the number of edges and V is the number of vertices
    for u, v, weight in edges:
        # Check if including this edge creates a cycle using union-find
        if ds.find(u) != ds.find(v):
            # If it doesn't form a cycle, include this edge in the MST
            ds.union(u, v)
            mst.append((u, v, weight))  # Add edge (u, v) to MST
            total_weight += weight  # Add the weight of the edge to the total weight

    # Return the MST and its total weight
    return mst, total_weight

# Example usage
edges = [
    (0, 1, 10),  # Edge between 0 and 1 with weight 10
    (0, 2, 6),   # Edge between 0 and 2 with weight 6
    (0, 3, 5),   # Edge between 0 and 3 with weight 5
    (1, 3, 15),  # Edge between 1 and 3 with weight 15
    (2, 3, 4)    # Edge between 2 and 3 with weight 4
]

n = 4  # Number of vertices
mst, total_weight = kruskal(n, edges)

# Output the edges of the Minimum Spanning Tree
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")
print(f"Total weight of the Minimum Spanning Tree: {total_weight}")

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Sorting the edges by weight:
#    - Time complexity: O(E log E), where E is the number of edges.
#    - Sorting is the most time-consuming part of Kruskal's algorithm.

# 2. Union-Find operations:
#    - Time complexity: O(E log V), where E is the number of edges and V is the number of vertices.
#    - Each union and find operation takes almost constant time, amortized over multiple operations (with path compression and union by rank).

# Overall time complexity:
# - Best-case time complexity: O(E log E), since sorting dominates and union-find is near constant.
# - Average-case time complexity: O(E log E).
# - Worst-case time complexity: O(E log E), where E is the number of edges.

# Space complexity:
# - Space complexity: O(V + E), where V is the number of vertices (for union-find data structures) and E is the number of edges (for storing edges).
