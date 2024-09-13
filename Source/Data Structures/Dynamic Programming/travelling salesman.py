import numpy as np

def traveling_salesman_dp(distances):
    """
    Solves the Traveling Salesman Problem using Dynamic Programming (Held-Karp algorithm).

    :param distances: A 2D array where distances[i][j] represents the distance between city i and city j
    :return: The minimum cost of visiting all cities and returning to the start
    """
    n = len(distances)  # Number of cities

    # Create a DP table with dimensions (2^n) x n, initialized to infinity
    # dp[mask][u] will store the minimum cost to reach city u with visited set 'mask'
    # Time complexity: O(2^n * n), as we need to process all subsets and cities
    dp = np.full((1 << n, n), float('inf'))  # (1 << n) represents 2^n subsets of cities
    dp[1][0] = 0  # Starting at city 0 with only city 0 visited

    # Iterate over all subsets of visited cities
    # Time complexity: O(2^n * n^2), where 2^n represents all subsets and n^2 represents the transitions between cities
    for mask in range(1 << n):  # Iterate through all subsets of cities (from 0 to 2^n - 1)
        for u in range(n):  # Iterate over all cities
            if mask & (1 << u):  # Check if city 'u' is in the current subset 'mask'
                for v in range(n):  # Iterate over all other cities
                    if not (mask & (1 << v)):  # Check if city 'v' is not in the current subset 'mask'
                        # Create a new subset by including city 'v' in the current set
                        new_mask = mask | (1 << v)
                        # Update the DP table with the minimum cost of reaching city 'v'
                        dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + distances[u][v])

    # Find the minimum cost to complete the tour and return to the start city (city 0)
    min_cost = float('inf')
    final_mask = (1 << n) - 1  # All cities are visited (the mask is now 2^n - 1)

    # Iterate over all cities (except city 0) to find the minimum cost to return to the start
    for u in range(1, n):
        # The cost to complete the tour by returning to city 0
        min_cost = min(min_cost, dp[final_mask][u] + distances[u][0])

    return min_cost  # Return the minimum cost of completing the tour

# Example usage
distances = [
    [0, 10, 15, 20],  # Distance from city 0 to other cities
    [10, 0, 35, 25],  # Distance from city 1 to other cities
    [15, 35, 0, 30],  # Distance from city 2 to other cities
    [20, 25, 30, 0]   # Distance from city 3 to other cities
]

# Solve the TSP using dynamic programming
min_cost = traveling_salesman_dp(distances)
print(f"Minimum cost to complete the tour: {min_cost}")

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Initializing the DP table:
#    - Time complexity: O(2^n * n), as the table has dimensions (2^n) x n and we initialize all entries to infinity.

# 2. Filling the DP table:
#    - Time complexity: O(2^n * n^2), as we iterate over all 2^n subsets and for each subset, we check the transitions
#      between every pair of cities. There are n^2 possible transitions (u to v).

# 3. Calculating the minimum cost to complete the tour:
#    - Time complexity: O(n), as we iterate over all cities to find the minimum cost of returning to the start city.

# Overall time complexity:
# - Best-case time complexity: O(2^n * n^2), since the Held-Karp algorithm processes all subsets and all transitions
#   between cities regardless of the input size.
# - Average-case time complexity: O(2^n * n^2).
# - Worst-case time complexity: O(2^n * n^2), as the algorithm must evaluate all possible subsets of cities and transitions.

# Space complexity:
# - Space complexity: O(2^n * n), as the DP table stores the minimum cost for all subsets of cities and all cities.
#   This requires 2^n rows (one for each subset) and n columns (one for each city).
