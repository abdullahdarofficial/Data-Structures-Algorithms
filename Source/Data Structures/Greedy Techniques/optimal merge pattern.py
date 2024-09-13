import heapq  # Import heapq to use a min-heap

def optimal_merge_pattern(file_sizes):
    """
    Computes the minimum cost to merge all files using the optimal merge pattern.

    :param file_sizes: List of integers representing the sizes of files
    :return: The minimum cost to merge all files
    """
    # Step 1: Convert the list of file sizes into a min-heap
    # Time complexity: O(n), where n is the number of file sizes
    heapq.heapify(file_sizes)

    total_cost = 0  # Initialize the total cost to zero

    # Step 2: Continue merging files until only one file remains
    # Time complexity: O(n log n), where n is the number of file sizes
    while len(file_sizes) > 1:
        # Step 3: Extract the two smallest files
        # Time complexity for heappop: O(log n)
        first_smallest = heapq.heappop(file_sizes)  # Smallest file
        second_smallest = heapq.heappop(file_sizes)  # Second smallest file

        # Step 4: Merge the two files and calculate the cost
        merge_cost = first_smallest + second_smallest  # Cost of merging the two files
        total_cost += merge_cost  # Add the merge cost to the total cost

        # Step 5: Add the merged file back into the heap
        # Time complexity for heappush: O(log n)
        heapq.heappush(file_sizes, merge_cost)

    # Return the total minimum cost of merging all files
    return total_cost

# Example usage
file_sizes = [4, 8, 6, 12, 10]  # List of file sizes
min_cost = optimal_merge_pattern(file_sizes)

# Output the minimum cost to merge all files
print(f"Minimum cost to merge all files: {min_cost}")

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Converting the list of file sizes into a min-heap:
#    - Time complexity: O(n), where n is the number of file sizes.
#    - This is the cost of heapifying the initial list of file sizes.

# 2. Merging files:
#    - Time complexity: O(n log n), where n is the number of file sizes.
#    - We merge files repeatedly until only one file remains. Each merge involves popping the two smallest files (O(log n) for each pop) and pushing the merged file back (O(log n)).
#    - Since we perform this merging operation n-1 times, the total complexity is O(n log n).

# Overall time complexity:
# - Best-case time complexity: O(n log n), as we must heapify and perform n-1 merge operations.
# - Average-case time complexity: O(n log n).
# - Worst-case time complexity: O(n log n).

# Space complexity:
# - Space complexity: O(n), since we store the file sizes in the heap and maintain the total cost.
