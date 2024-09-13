def multi_stage_graph_shortest_path(graph, stages):
    """
    Find the shortest path in a multi-stage graph.

    :param graph: Dictionary where graph[i][j] represents the weight of the edge from node i to node j
    :param stages: List of lists where each sublist represents nodes in that stage
    :return: Tuple containing the shortest path distance and the path taken
    """
    n = len(stages)  # Number of stages in the graph
    INF = float('inf')  # Define a large number to represent infinity

    # Create a DP table to store shortest distances to nodes in each stage
    # Time complexity: O(n*m), where n is the number of stages and m is the maximum number of nodes in a stage
    dp = [[INF] * len(stage) for stage in stages]  # Initialize the DP table with infinity

    # The cost to reach any node in the last stage is 0, as it's the destination
    # Time complexity: O(m_last), where m_last is the number of nodes in the last stage
    for j in range(len(stages[-1])):
        dp[-1][j] = 0  # The cost to reach the destination nodes is 0

    # Fill the DP table from the second-last stage to the first stage
    # Time complexity: O(n * m^2), where n is the number of stages and m is the number of nodes per stage
    for i in range(n - 2, -1, -1):  # Iterate over the stages in reverse order
        for j in range(len(stages[i])):  # For each node in the current stage
            # Find the minimum cost to reach any node in the next stage
            for k in range(len(stages[i + 1])):  # For each node in the next stage
                if graph[stages[i][j]].get(stages[i + 1][k], INF) != INF:
                    dp[i][j] = min(dp[i][j], graph[stages[i][j]][stages[i + 1][k]] + dp[i + 1][k])

    # Backtrack to find the path from the source to the destination
    path = []
    min_cost = min(dp[0])  # Find the minimum cost from the start node
    current_node = dp[0].index(min_cost)  # Find the starting node index
    path.append(stages[0][current_node])  # Add the starting node to the path

    # Reconstruct the path by following the minimum cost decisions
    for i in range(1, n):
        for j in range(len(stages[i])):
            if dp[i - 1][current_node] + graph[stages[i - 1][current_node]].get(stages[i][j], INF) == dp[i][j]:
                path.append(stages[i][j])  # Add the next node in the path
                current_node = j  # Move to the next node
                break

    return min_cost, path  # Return the minimum cost and the path taken

# Example usage
graph = {
    0: {1: 2, 2: 4},   # Edges from node 0 to 1 and 2
    1: {3: 7, 4: 1},   # Edges from node 1 to 3 and 4
    2: {4: 3},         # Edge from node 2 to 4
    3: {5: 1},         # Edge from node 3 to 5
    4: {5: 5},         # Edge from node 4 to 5
    5: {}              # Node 5 is the destination with no outgoing edges
}

# Define stages as lists of nodes
stages = [
    [0],      # Stage 1 (source)
    [1, 2],   # Stage 2
    [3, 4],   # Stage 3
    [5]       # Stage 4 (destination)
]

# Call the function to find the shortest path
min_cost, path = multi_stage_graph_shortest_path(graph, stages)
print(f"Minimum cost: {min_cost}")
print(f"Path taken: {path}")

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Initializing the DP table:
#    - Time complexity: O(n * m), where n is the number of stages and m is the maximum number of nodes per stage.
#    - This is because we initialize a DP table of size (number of stages) x (number of nodes in each stage).

# 2. Filling the DP table:
#    - Time complexity: O(n * m^2), where n is the number of stages and m is the maximum number of nodes in each stage.
#    - For each node in stage i, we check the cost to reach each node in stage i+1, which results in an O(m^2) term.

# 3. Backtracking to find the path:
#    - Time complexity: O(n * m), where n is the number of stages and m is the maximum number of nodes per stage.
#    - This is because we iterate over the DP table to reconstruct the path.

# Overall time complexity:
# - Best-case time complexity: O(n * m^2), where n is the number of stages and m is the maximum number of nodes in a stage.
# - Average-case time complexity: O(n * m^2).
# - Worst-case time complexity: O(n * m^2), as we need to evaluate all possible connections between nodes in adjacent stages.

# Space complexity:
# - Space complexity: O(n * m), where n is the number of stages and m is the maximum number of nodes per stage.
# - This is because the DP table requires space proportional to the number of stages and the number of nodes in each stage.
