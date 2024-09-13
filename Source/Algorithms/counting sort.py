def counting_sort(arr):
    # Find the maximum and minimum elements in the array
    # This is necessary to determine the range of the count array
    # Time complexity: O(n), where n is the length of the input array
    max_val = max(arr)  # Get the maximum value in the array
    min_val = min(arr)  # Get the minimum value in the array (to handle negative numbers)

    # Create a count array to store the frequency of each unique element
    # The size of the count array is based on the range of the input values
    # Time complexity: O(max_val - min_val), which depends on the range of values
    count_range = max_val - min_val + 1  # Range of the values (handles negative values)
    count = [0] * count_range  # Initialize the count array with zeros

    # Store the count of each element in the input array
    # The index in the count array is calculated by subtracting the min_val to handle negative indices
    # Time complexity: O(n), as we iterate over the input array once
    for num in arr:
        count[num - min_val] += 1  # Increment the count for the element 'num'

    # Modify the count array by calculating the cumulative sum of counts
    # This will help place elements in their correct positions in the sorted array
    # Time complexity: O(max_val - min_val), as we process the count array
    for i in range(1, len(count)):
        count[i] += count[i - 1]  # Add the count of the previous element to the current one

    # Create an output array to store the sorted elements
    # Time complexity: O(n), as the size of the output array is the same as the input array
    output = [0] * len(arr)

    # Build the output array by placing elements at their correct positions
    # The position is determined using the cumulative counts from the count array
    # We iterate in reverse to maintain stability (order of duplicate elements)
    # Time complexity: O(n)
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num  # Place the element in the correct sorted position
        count[num - min_val] -= 1  # Decrement the count for this element

    # Copy the sorted output array back to the original array
    # Time complexity: O(n)
    for i in range(len(arr)):
        arr[i] = output[i]  # Copy the sorted elements back to the original array

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort(arr)
print("Sorted array:", arr)

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Finding the maximum and minimum values:
#    - Time complexity: O(n), where n is the length of the input array.
#    - Best, Average, and Worst-case: O(n), as we must scan the entire array to find the min and max.

# 2. Creating the count array:
#    - Time complexity: O(max_val - min_val), which is the size of the range of the input values.
#    - Best, Average, and Worst-case: O(max_val - min_val).

# 3. Counting the occurrences of each element:
#    - Time complexity: O(n), as we iterate through the input array to populate the count array.
#    - Best, Average, and Worst-case: O(n).

# 4. Modifying the count array to store cumulative counts:
#    - Time complexity: O(max_val - min_val), as we process the count array.
#    - Best, Average, and Worst-case: O(max_val - min_val).

# 5. Building the output array:
#    - Time complexity: O(n), as we iterate over the input array in reverse to build the sorted array.
#    - Best, Average, and Worst-case: O(n).

# 6. Copying the sorted array back to the original array:
#    - Time complexity: O(n), as we copy the sorted elements back into the input array.
#    - Best, Average, and Worst-case: O(n).

# Overall time complexity:
# - The overall time complexity is O(n + max_val - min_val), where n is the size of the input array and (max_val - min_val) is the range of input values.
# - Best-case time complexity: O(n + k), where k = max_val - min_val.
# - Average-case time complexity: O(n + k).
# - Worst-case time complexity: O(n + k), which occurs when the range of values is large but the array is small.
