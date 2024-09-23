
def knapsack_recursive(weights, profits, capacity, index = 0):
    if index == len(weights) or index == len(profits):
        return 0
    elif weights[index] > capacity:
        return knapsack_recursive(weights, profits, capacity, index + 1)
    else:
        return max(
            profits[index] + knapsack_recursive(weights, profits, capacity - weights[index], index + 1),
            knapsack_recursive(weights, profits, capacity, index + 1)
        )


def is_knapsack_profitable(weights, profits, capacity):
    # Call the knapsack function and check if the result is non-zero
    result = knapsack_recursive(weights, profits, capacity)
    return result > 0

# Example usage
weights = [1, 2, 3]
profits = [6, 10, 12]
capacity = 5

if is_knapsack_profitable(weights, profits, capacity):
    print("Profitable")
else:
    print("Not profitable")
