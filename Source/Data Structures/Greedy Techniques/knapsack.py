class Item:
    def __init__(self, value, weight):
        self.value = value  # Value of the item
        self.weight = weight  # Weight of the item
        # Calculate the value per unit weight for easy comparison
        self.value_per_weight = value / weight

def fractional_knapsack(items, capacity):
    """
    Solves the Fractional Knapsack problem using a greedy approach.

    :param items: List of Item objects, each with a value and weight
    :param capacity: Maximum weight capacity of the knapsack
    :return: Maximum value that can be obtained by filling the knapsack
    """
    # Step 1: Sort items by value per weight in descending order
    # Time complexity: O(n log n), where n is the number of items, due to sorting
    items.sort(key=lambda x: x.value_per_weight, reverse=True)

    total_value = 0  # To track the total value in the knapsack

    # Step 2: Iterate through sorted items
    # Time complexity: O(n), where n is the number of items
    for item in items:
        # If the knapsack is full (capacity is 0), stop adding items
        if capacity == 0:
            break

        # Step 3: Take as much of the current item as possible
        take_weight = min(item.weight, capacity)  # Take the minimum of the item's weight or remaining capacity
        total_value += take_weight * item.value_per_weight  # Add the value of the fraction taken to the total value
        capacity -= take_weight  # Reduce the remaining capacity of the knapsack

    # Return the total value obtained by filling the knapsack
    return total_value

# Example usage
items = [
    Item(60, 10),   # Item with value 60 and weight 10
    Item(100, 20),  # Item with value 100 and weight 20
    Item(120, 30)   # Item with value 120 and weight 30
]

capacity = 50  # Maximum weight capacity of the knapsack
max_value = fractional_knapsack(items, capacity)  # Solve the Fractional Knapsack problem

# Output the maximum value that can be obtained
print(f"Maximum value that can be obtained: {max_value}")

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Sorting the items by value per weight:
#    - Time complexity: O(n log n), where n is the number of items.
#    - This is due to sorting the items based on their value-to-weight ratio.

# 2. Iterating through the sorted items:
#    - Time complexity: O(n), where n is the number of items.
#    - We iterate through each item and decide how much of it to take, which is a constant-time operation per item.

# Overall time complexity:
# - Best-case time complexity: O(n log n), since sorting dominates the time complexity.
# - Average-case time complexity: O(n log n).
# - Worst-case time complexity: O(n log n), as the sorting operation is the most time-consuming step.

# Space complexity:
# - Space complexity: O(1), assuming sorting is done in-place and no additional data structures are used apart from the input list.
# - If not in-place sorting, the space complexity can go up to O(n) for the auxiliary data structures used for sorting.
