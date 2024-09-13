# Class to represent each item in the knapsack
class KnapsackItem:
    def __init__(self, weight, value):
        # Initialize with weight and value for each item
        self.weight = weight
        self.value = value

# Node class to represent the nodes in the decision tree (used in branch and bound)
class Node:
    def __init__(self, level, value, weight, bound):
        # Level in the decision tree
        self.level = level
        # Current value of the knapsack at this node
        self.value = value
        # Current weight of the knapsack at this node
        self.weight = weight
        # Upper bound of the maximum value that can be achieved from this node
        self.bound = bound

    # Function to calculate the upper bound on the maximum value (used in branch and bound)
def bound(u, n, capacity, items):
    # If the weight of the node exceeds the capacity, return 0 (invalid)
    if u.weight >= capacity:
        return 0

    # Initial profit bound is the current value at node u
    profit_bound = u.value
    j = u.level + 1  # Start from the next level
    total_weight = u.weight  # Track the total weight so far

    # Greedily add items until the capacity is reached
    while j < n and total_weight + items[j].weight <= capacity:
        total_weight += items[j].weight
        profit_bound += items[j].value
        j += 1

    # If we can't add the next full item, add a fractional part of the item
    if j < n:
        profit_bound += (capacity - total_weight) * items[j].value / items[j].weight

    return profit_bound  # Return the upper bound on the value

# Function to solve the 0/1 knapsack problem using the branch and bound method
def knapsack_branch_and_bound(capacity, items):
    # Sort the items by their value-to-weight ratio in decreasing order (greedy heuristic)
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    Q = []  # Priority queue to store nodes
    n = len(items)  # Number of items

    # Initialize starting node u and another node v for branching
    u = Node(-1, 0, 0, 0)  # u is at level -1 with value 0, weight 0, and bound 0
    v = Node(-1, 0, 0, 0)  # v is a temporary node for branching decisions
    u.bound = bound(u, n, capacity, items)  # Calculate bound for the root node

    Q.append(u)  # Add the root node to the priority queue
    max_profit = 0  # Track the maximum profit found

    # Explore the nodes in the priority queue
    while Q:
        u = Q.pop(0)  # Dequeue the next node

        # If u is at the root, move to the first level
        if u.level == -1:
            v.level = 0
        # If u is the last item, skip processing
        if u.level == n - 1:
            continue

        # Branch: include the next item
        v.level = u.level + 1
        v.weight = u.weight + items[v.level].weight
        v.value = u.value + items[v.level].value

        # If the weight is within capacity and value is greater, update max_profit
        if v.weight <= capacity and v.value > max_profit:
            max_profit = v.value

        # Calculate bound for node where the item is included
        v.bound = bound(v, n, capacity, items)

        # If the bound is promising, add the node to the queue
        if v.bound > max_profit:
            Q.append(v)

        # Branch: exclude the next item (undo weight and value change)
        v.weight = u.weight
        v.value = u.value
        v.bound = bound(v, n, capacity, items)

        # If the bound is promising, add the node to the queue
        if v.bound > max_profit:
            Q.append(v)

    return max_profit  # Return the maximum profit found

# Example usage
items = [KnapsackItem(2, 40), KnapsackItem(3, 50), KnapsackItem(5, 100), KnapsackItem(7, 120)]
capacity = 10
max_value = knapsack_branch_and_bound(capacity, items)
print(f"Maximum value in knapsack: {max_value}")

# -------------------------------
# Time complexity analysis:
# -------------------------------
# bound() function:
# - The while loop inside this function can run at most 'n' times, where n is the number of items.
# - Calculating the fractional part of the item is an O(1) operation.
# - Hence, the time complexity of bound() is O(n).

# knapsack_branch_and_bound() function:
# - Sorting the items by value-to-weight ratio takes O(n log n).
# - In the worst case, the priority queue can have 2^n nodes, and for each node, we calculate the bound,
#   which is O(n). Hence, the worst-case time complexity of the branch and bound algorithm is O(n * 2^n).
# - Best-case scenario: If the first few branches lead to a quick solution, the complexity can reduce
#   significantly.
# - Average-case: O(n * 2^n) but typically much faster in practical scenarios due to pruning of non-promising branches.

# Best case time complexity: O(n log n) (if optimal solution is found early)
# Average case time complexity: O(n * 2^n) (with pruning helping reduce the search space)
# Worst case time complexity: O(n * 2^n) (exploring all branches without pruning)
