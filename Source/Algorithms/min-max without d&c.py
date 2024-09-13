def find_min_max(arr):
    # Initialize min and max with the first element of the array
    # Time complexity: O(1), constant time initialization
    min_val = arr[0]
    max_val = arr[0]

    # Traverse the array starting from the second element
    # Time complexity: O(n), where n is the length of the array
    for num in arr[1:]:
        # If the current element is smaller than the current minimum, update min_val
        if num < min_val:
            min_val = num
        # If the current element is larger than the current maximum, update max_val
        if num > max_val:
            max_val = num

    # Return the minimum and maximum values found
    return min_val, max_val

# Example usage
arr = [3, 5, 1, 8, 2, 9, 4, 7]
min_val, max_val = find_min_max(arr)
print(f"Minimum value: {min_val}")
print(f"Maximum value: {max_val}")

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Initializing min_val and max_val:
#    - Time complexity: O(1), constant time to assign the first element of the array to both min_val and max_val.

# 2. Traversing the array:
#    - Time complexity: O(n), where n is the length of the array.
#    - We iterate through the array starting from the second element and compare each element to min_val and max_val.

# Overall time complexity:
# - Best-case time complexity: O(n), as we need to traverse the entire array regardless of the order of the elements.
# - Average-case time complexity: O(n), as each element needs to be compared with the current min and max values.
# - Worst-case time complexity: O(n), since we must check every element to ensure we find the minimum and maximum values.

# Space complexity:
# - The space complexity is O(1), as the algorithm only uses a few variables (min_val, max_val) and does not require any additional space proportional to the input size.
