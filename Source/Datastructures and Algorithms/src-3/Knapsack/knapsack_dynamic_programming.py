def is_knapsack_profitable(weights, profits, capacity):
    # table = [x for x in range(columns) for x in range(rows)]
    table = [[0 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]

    for i in range(len(weights)):
        for j in range(1, capacity + 1):
            if weights[i] > j:
                table[i + 1][j] = table[i][j]
            else:
                table[i + 1][j] = max(table[i][j], profits[i] + table[i][j - weights[i]])

    return table[-1][-1]

# Example usage
weights = [1, 2, 3]
profits = [6, 10, 12]
capacity = 5

if is_knapsack_profitable(weights, profits, capacity):
    print("Profitable")
else:
    print("Not profitable")
