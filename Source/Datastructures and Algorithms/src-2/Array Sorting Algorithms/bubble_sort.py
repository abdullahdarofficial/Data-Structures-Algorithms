def bubble_sort(arr):
    # Time Complexity: O(n) best case, O(n^2) worst and average case
    # Best case occurs when the array is already sorted
    # Worst and average case occur when the array is unsorted or reverse sorted

    n = len(arr)  # Get the length of the array (Time complexity: O(1))

    # Outer loop for each pass over the array
    for i in range(n):  # Loop runs n times (Time complexity: O(n))

        swapped = False  # Flag to track if any swapping occurs (Time complexity: O(1))

        # Inner loop goes up to the last unsorted element (each pass reduces the unsorted portion)
        for j in range(n - 1 - i):  # Time complexity: O(n) in the first iteration, reducing by 1 in each subsequent pass
            if arr[j] > arr[j + 1]:  # Compare adjacent elements (Time complexity: O(1))
                # Swap the elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements (Time complexity: O(1))
                swapped = True  # Set flag to True indicating a swap occurred (Time complexity: O(1))

        # If no two elements were swapped in this iteration, the array is sorted
        if not swapped:  # Break early if no swaps happened (Time complexity: O(1))
            break  # Time complexity: O(1)

    return arr  # Return the sorted array (Time complexity: O(1))

arr = [5, 3, 6, 15, 2, 67, 3, 1, 6, 32, 0, 24, 21, 56, 231, 9, 34]  # Array to be sorted
print("Original array:", arr)  # Print original array (Time complexity: O(n))
print("Bubble Sort")  # Print operation name (Time complexity: O(1))
sorted_arr = bubble_sort(arr)  # Call the bubble_sort function (Time complexity: Best case: O(n), Worst case: O(n^2))
print(sorted_arr)  # Print the sorted array (Time complexity: O(n))

# Time Complexity Analysis:
# Best Case: O(n) - The array is already sorted, so the inner loop doesn't perform any swaps and breaks early.
# Average Case: O(n^2) - On average, the array requires multiple swaps, and the nested loops contribute to quadratic time complexity.
# Worst Case: O(n^2) - If the array is in reverse order, the inner loop will perform swaps for every comparison, resulting in O(n^2).
