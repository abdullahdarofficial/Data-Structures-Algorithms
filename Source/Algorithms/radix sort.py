# Function to do counting sort based on the digit represented by exp (10^i)
def counting_sort(arr, exp):
    n = len(arr)  # Number of elements in the array

    # Output array to store the sorted order
    # Time complexity: O(n), where n is the length of the array
    output = [0] * n  # Initialize the output array to store the sorted elements

    # Initialize count array with zeros (for digits 0 to 9)
    # Time complexity: O(1), as the size of count array is fixed at 10
    count = [0] * 10  # Count array for digits (0 to 9)

    # Store the count of occurrences of digits (0 to 9) for the current digit (exp)
    # Time complexity: O(n), where n is the length of the array
    for i in range(n):
        index = arr[i] // exp  # Extract the digit at the current exponent (exp)
        count[index % 10] += 1  # Increment the count for the digit

    # Modify the count array such that each position contains the actual position
    # of the digit in the output array
    # Time complexity: O(1), as we only loop through the count array (size 10)
    for i in range(1, 10):
        count[i] += count[i - 1]  # Update count[i] to hold cumulative counts

    # Build the output array using the count array
    # Time complexity: O(n), where n is the length of the array
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp  # Extract the digit at the current exponent (exp)
        output[count[index % 10] - 1] = arr[i]  # Place the element at its sorted position
        count[index % 10] -= 1  # Decrement the count for that digit

    # Copy the sorted numbers from the output array back to the original array
    # Time complexity: O(n), where n is the length of the array
    for i in range(n):
        arr[i] = output[i]  # Update the original array with the sorted order

# Main radix sort function
def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    # Time complexity: O(n), where n is the length of the array
    max_val = max(arr)  # Maximum value in the array determines the number of digits

    # Perform counting sort for every digit. exp is 10^i (1, 10, 100, ...)
    # Time complexity: O(d * (n + k)), where d is the number of digits, n is the length of the array,
    # and k is the range of the digits (0-9, so k is constant)
    exp = 1  # Start with the least significant digit (1s place)
    while max_val // exp > 0:
        counting_sort(arr, exp)  # Sort based on the current digit (exp)
        exp *= 10  # Move to the next digit (10s, 100s, etc.)

# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", arr)
radix_sort(arr)
print("Sorted array:", arr)

# -------------------------------
# Time complexity analysis:
# -------------------------------

# counting_sort() function:
# 1. Initializing the output array and count array:
#    - Time complexity: O(n), where n is the size of the input array, to initialize the output array.
#    - Initializing the count array takes O(1) time since the size is fixed at 10.
#
# 2. Counting occurrences of each digit:
#    - Time complexity: O(n), as we iterate through the input array once.
#
# 3. Modifying the count array to store cumulative counts:
#    - Time complexity: O(1), as the count array has a fixed size of 10, making this operation constant time.
#
# 4. Building the output array:
#    - Time complexity: O(n), as we iterate through the input array in reverse order.
#
# 5. Copying the output array back to the original array:
#    - Time complexity: O(n), as we copy the sorted elements back to the original array.

# Overall time complexity of counting_sort():
# - Best, average, and worst-case time complexity: O(n), as each step takes linear time relative to the input size.

# radix_sort() function:
# 1. Finding the maximum value in the array:
#    - Time complexity: O(n), as we iterate through the array once to find the maximum value.
#
# 2. Sorting by each digit using counting_sort():
#    - For each digit, we perform counting_sort(), which takes O(n) time for each iteration.
#    - The number of digits (d) in the maximum value is log(max_val), or more precisely, the number of digits is proportional to the number of iterations.
#
# Overall time complexity of radix_sort():
# - Since counting_sort() is performed for each digit, the total time complexity is O(d * n), where d is the number of digits and n is the size of the array.
# - In this case, d is usually considered constant for practical values (e.g., integers with a fixed number of digits), so the overall time complexity can be approximated to O(n).
#
# Best-case time complexity: O(n), where n is the size of the array and d is constant.
# Average-case time complexity: O(n), since the number of digits is fixed and each digit takes linear time to sort.
# Worst-case time complexity: O(n), as radix sort always processes all digits, and counting sort is O(n) per digit.

# Space complexity:
# - The space complexity is O(n) due to the output array and the count array used in counting_sort().
# - Radix sort is not an in-place sorting algorithm as it requires additional space for the output array.
