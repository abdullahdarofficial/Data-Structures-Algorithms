import math

# Class to represent the Traveling Salesman Problem (TSP) solver
class TSP:
    def __init__(self, n, distance_matrix):
        # Initialize the number of cities (n) and the distance matrix
        self.n = n  # number of cities
        self.distance_matrix = distance_matrix  # matrix representing distances between cities

    # Helper function to calculate a lower bound on the minimum cost for a given partial path
    def calculate_lower_bound(self, level, current_cost, visited):
        # Start with the current cost of the path so far
        bound = current_cost
        # Iterate over all cities to compute a lower bound by adding the minimum outgoing edge cost for unvisited cities
        for i in range(self.n):
            if not visited[i]:
                # Add the minimum cost edge for unvisited cities to the lower bound
                bound += self.minimum_edge_cost(i, visited)
        return bound  # Return the calculated lower bound

    # Get the minimum outgoing edge cost for a given city, ignoring already visited cities
    def minimum_edge_cost(self, city, visited):
        # Initialize min_cost with infinity
        min_cost = math.inf
        # Check all cities to find the minimum cost outgoing edge for 'city', ignoring visited cities
        for i in range(self.n):
            if not visited[i] and city != i:
                # Update min_cost if a lower cost is found
                min_cost = min(min_cost, self.distance_matrix[city][i])
        return min_cost  # Return the minimum cost outgoing edge

    # Branch and Bound solution to solve the TSP problem
    def tsp_branch_and_bound(self):
        # Initialize the visited array to track cities that have been visited
        visited = [False] * self.n
        # Mark the first city (city 0) as visited
        visited[0] = True
        # Initialize min_cost with infinity to store the minimum cost of the tour
        min_cost = math.inf
        # Initialize the route array to store the final optimal route
        route = [-1] * self.n

        # Helper function to recursively explore the branches in the branch-and-bound tree
        def branch_and_bound(current_city, level, current_cost, path):
            nonlocal min_cost, route  # Access min_cost and route in the outer function

            # Base case: If we have visited all cities, complete the tour by returning to the starting city
            if level == self.n:
                # Calculate the total cost of the tour by returning to the starting city
                total_cost = current_cost + self.distance_matrix[current_city][0]
                # If the total cost is less than the current minimum cost, update min_cost and save the route
                if total_cost < min_cost:
                    min_cost = total_cost
                    route = path[:]  # Make a copy of the current path to save it as the optimal route
                return

            # Explore the next unvisited cities from the current city
            for next_city in range(self.n):
                if not visited[next_city]:
                    # Mark the next city as visited
                    visited[next_city] = True
                    # Add the next city to the current path
                    path[level] = next_city

                    # Calculate the new cost of visiting the next city
                    new_cost = current_cost + self.distance_matrix[current_city][next_city]
                    # Calculate the lower bound for this partial solution
                    bound = self.calculate_lower_bound(level + 1, new_cost, visited)

                    # Prune the branch if the lower bound exceeds the current minimum cost
                    if bound < min_cost:
                        # Recursively explore the next city
                        branch_and_bound(next_city, level + 1, new_cost, path)

                    # Backtrack: unmark the next city as visited to explore other possibilities
                    visited[next_city] = False

        # Start the recursive exploration from the first city
        path = [0] * self.n  # Initialize the path with the starting city
        branch_and_bound(0, 1, 0, path)  # Start recursion with city 0, level 1, and cost 0
        return min_cost, route  # Return the minimum cost and the optimal route

# Example usage: Solving TSP for a distance matrix
distance_matrix = [
    [0, 10, 15, 20],  # Distance from city 0 to other cities
    [10, 0, 35, 25],  # Distance from city 1 to other cities
    [15, 35, 0, 30],  # Distance from city 2 to other cities
    [20, 25, 30, 0]   # Distance from city 3 to other cities
]

# Create an instance of the TSP solver
tsp_solver = TSP(4, distance_matrix)
# Solve the TSP using branch and bound
min_cost, optimal_route = tsp_solver.tsp_branch_and_bound()

# Output the results
print(f"Minimum cost: {min_cost}")
print(f"Optimal route: {optimal_route}")

# -------------------------------
# Time complexity analysis:
# -------------------------------

# calculate_lower_bound() function:
# - This function iterates over all cities to calculate the minimum edge cost for each unvisited city.
# - The minimum_edge_cost() function is called n times, where n is the number of cities.
# - Time complexity of calculate_lower_bound() is O(n^2), where n is the number of cities.

# minimum_edge_cost() function:
# - The function iterates over all cities to find the minimum outgoing edge for a given city.
# - Time complexity of minimum_edge_cost() is O(n), where n is the number of cities.

# tsp_branch_and_bound() function:
# - The branch_and_bound() recursive function explores all possible paths between cities.
# - In the worst case, it explores all n! possible tours, since there are n! permutations of cities in the TSP.
# - For each tour, the calculate_lower_bound() function is called, which has a complexity of O(n^2).
# - Hence, the worst-case time complexity of tsp_branch_and_bound() is O(n! * n^2).

# Best case time complexity: O(n^2) (if the optimal path is found early and many branches are pruned).
# Average case time complexity: O(n! * n^2) (with pruning reducing the search space in practice).
# Worst case time complexity: O(n! * n^2) (exploring all possible city permutations).
