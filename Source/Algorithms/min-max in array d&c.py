def find_min_max(arr, low, high):
    # Base case: If the array contains only one element
    # Time complexity: O(1) (constant time operation)
    if low == high:
        # Return the single element as both minimum and maximum
        return arr[low], arr[low]

    # Base case: If the array contains two elements
    # Time complexity: O(1) (constant time operation)
    elif high == low + 1:
        # Compare the two elements and return the minimum and maximum
        if arr[low] < arr[high]:
            return arr[low], arr[high]  # First element is smaller
        else:
            return arr[high], arr[low]  # Second element is smaller

    # Recursive case: If the array contains more than two elements
    else:
        # Find the middle index to divide the array into two halves
        mid = (low + high) // 2

        # Recursively find the minimum and maximum in the left half
        left_min, left_max = find_min_max(arr, low, mid)

        # Recursively find the minimum and maximum in the right half
        right_min, right_max = find_min_max(arr, mid + 1, high)

        # Find the overall minimum by comparing the left and right halves
        overall_min = min(left_min, right_min)

        # Find the overall maximum by comparing the left and right halves
        overall_max = max(left_max, right_max)

        # Return the overall minimum and maximum
        return overall_min, overall_max

# Example usage
arr = [3, 5, 1, 8, 2, 9, 4, 7]
min_val, max_val = find_min_max(arr, 0, len(arr) - 1)
print(f"Minimum value: {min_val}")
print(f"Maximum value: {max_val}")

# -------------------------------
# Time complexity analysis:
# -------------------------------

# The algorithm uses a divide-and-conquer approach, similar to merge sort, where the array is divided into two halves.
# Each recursive call handles half of the array, and then the results from both halves are combined.

# 1. Base case (single element or two elements):
#    - Time complexity: O(1), as the comparisons are constant time operations.

# 2. Recursive case:
#    - The array is divided into two halves, so for an array of size n, there are two recursive calls for n/2 elements.
#    - The combination step (comparing the minimum and maximum from both halves) takes constant time O(1).

# The recurrence relation for this approach is:
#    T(n) = 2T(n/2) + O(1)
#    - Solving this recurrence relation gives a time complexity of O(n).

# Overall time complexity:
# - Best-case time complexity: O(n), as we always divide the array into halves and make constant-time comparisons.
# - Average-case time complexity: O(n), as the recursive division and constant comparisons happen in all cases.
# - Worst-case time complexity: O(n), since the entire array needs to be processed, divided, and compared.

# Space complexity:
# - The space complexity is O(log n) due to the recursion stack depth in dividing the array into halves.
