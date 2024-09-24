def insertion_sort(arr):
    # Iterate over each element in the array starting from index 1
    # Time Complexity: O(n^2) worst and average case, O(n) best case (array already sorted)

    for i in range(1, len(arr)):  # Outer loop runs n-1 times (Time complexity: O(n))

        key = arr[i]  # The element to be positioned in the sorted part (Time complexity: O(1))
        j = i - 1     # Start comparing with the previous element (Time complexity: O(1))

        # Shift elements of the sorted portion of the array to the right to make space for key
        while j >= 0 and key < arr[j]:  # Compare key with sorted elements (Time complexity: O(n) in worst case)
            arr[j + 1] = arr[j]  # Move the larger element one position to the right (Time complexity: O(1))
            j -= 1  # Move one step left (Time complexity: O(1))

        # Insert the key at its correct position after shifting
        arr[j + 1] = key  # Insert key in the correct position (Time complexity: O(1))

    return arr  # Return the sorted array (Time complexity: O(1))

arr = [5, 3, 6, 15, 2, 67, 3, 1, 6, 32, 0, 24, 21, 56, 231, 9, 34]  # Array to be sorted
print("Original array:", arr)  # Print original array (Time complexity: O(n))
print("Insertion Sort")  # Print the sorting method (Time complexity: O(1))
sorted_arr = insertion_sort(arr)  # Call the insertion_sort function (Time complexity: Best case: O(n), Worst case: O(n^2))
print(sorted_arr)  # Print the sorted array (Time complexity: O(n))

# Time Complexity Analysis:
# Best Case: O(n) - If the array is already sorted, the while loop never runs and the outer loop runs n times.
# Average Case: O(n^2) - On average, the while loop runs for about half of the elements, resulting in O(n^2) time.
# Worst Case: O(n^2) - If the array is sorted in reverse order, the while loop shifts all elements for each insertion, leading to O(n^2).
