class Item:
    def __init__(self, value, weight):
        self.value = value  # The value of the item
        self.weight = weight  # The weight of the item
        # Calculate the value per weight unit for easy comparison
        self.value_per_weight = value / weight

def fractional_knapsack(items, capacity):
    # Sort items by value per weight in descending order
    # Time complexity: O(n log n), where n is the number of items
    # Sorting is done based on value_per_weight
    items.sort(key=lambda x: x.value_per_weight, reverse=True)

    total_value = 0  # Track the total value of the items taken

    # Iterate through the sorted items
    # Time complexity: O(n), where n is the number of items
    for item in items:
        if capacity == 0:
            break  # If the knapsack is full, stop

        # Determine how much of the current item can be taken
        take_weight = min(item.weight, capacity)  # Take as much as we can fit
        total_value += take_weight * item.value_per_weight  # Add the value of the portion taken
        capacity -= take_weight  # Reduce the remaining capacity

    # Return the maximum value that can be obtained
    return total_value

# Example usage
items = [
    Item(60, 10),  # value, weight
    Item(100, 20),
    Item(120, 30)
]

capacity = 50  # Maximum capacity of the knapsack

# Find the maximum value that can be obtained
max_value = fractional_knapsack(items, capacity)

print(f"Maximum value that can be obtained: {max_value}")

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Sorting the items by value per weight:
#    - Time complexity: O(n log n), where n is the number of items.
#    - This is because sorting the items involves comparing their value per weight ratios.

# 2. Iterating through the sorted items:
#    - Time complexity: O(n), where n is the number of items.
#    - In each iteration, we decide how much of the current item to take and update the total value and capacity.

# Overall time complexity:
# - Best-case time complexity: O(n log n), dominated by the sorting step.
# - Average-case time complexity: O(n log n), as the sorting step dominates regardless of input distribution.
# - Worst-case time complexity: O(n log n), since sorting is the most expensive operation in the algorithm.

# Space complexity:
# - Space complexity: O(1), as the algorithm uses a constant amount of extra space, aside from the input list.
#   If we count the space used to store the input, then the space complexity is O(n).
