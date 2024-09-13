def knapsack(values, weights, capacity):
    n = len(values)  # Number of items

    # Initialize a 2D DP array with zeros
    # dp[i][w] represents the maximum value we can achieve with the first 'i' items and capacity 'w'
    # Time complexity: O(n * capacity), as we create a 2D array with n+1 rows and capacity+1 columns
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the DP array from bottom up
    # Time complexity: O(n * capacity), where n is the number of items and capacity is the knapsack's capacity
    for i in range(1, n + 1):  # Iterate over each item
        for w in range(capacity + 1):  # Iterate over each possible capacity
            if weights[i - 1] <= w:
                # Option 1: Include the item if it fits in the knapsack
                include_item = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                # Option 2: Exclude the item
                exclude_item = dp[i - 1][w]
                # Choose the maximum of including or excluding the item
                dp[i][w] = max(include_item, exclude_item)
            else:
                # If the item cannot be included due to weight, just exclude it
                dp[i][w] = dp[i - 1][w]

    # The maximum value is in the bottom-right corner of the DP array
    return dp[n][capacity]  # Return the maximum value achievable with 'n' items and 'capacity' weight

# Example usage
values = [60, 100, 120]  # Values of the items
weights = [10, 20, 30]   # Weights of the items
capacity = 50            # Capacity of the knapsack

max_value = knapsack(values, weights, capacity)
print(f"Maximum value achievable: {max_value}")

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Initializing the DP table:
#    - Time complexity: O(n * capacity), where n is the number of items and capacity is the knapsack capacity.
#    - This involves creating a 2D array of size (n+1) x (capacity+1).

# 2. Filling the DP table:
#    - Time complexity: O(n * capacity), as we iterate through all 'n' items and for each item, we loop through
#      all capacities from 0 to the maximum capacity.
#    - For each combination of item and capacity, we make a constant-time decision between including or excluding the item.

# Overall time complexity:
# - Best-case time complexity: O(n * capacity), since every item and capacity combination is processed regardless of input.
# - Average-case time complexity: O(n * capacity), as the DP table must be filled for all items and capacities.
# - Worst-case time complexity: O(n * capacity), as we must check every possibility when building the table.

# Space complexity:
# - Space complexity: O(n * capacity), since the algorithm uses a 2D DP array of size (n+1) x (capacity+1).
# - The algorithm requires additional space to store the DP table, making it non-in-place.

# Alternative optimization:
# - We can reduce the space complexity to O(capacity) by using a 1D array instead of a 2D array, since the decision
#   at any point depends only on the previous row in the table.
