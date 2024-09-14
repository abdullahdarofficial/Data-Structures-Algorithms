def cal_rotations(arr):
    # Time Complexity: O(log n), where n is the size of the array (due to binary search approach).
    # Space Complexity: O(1), as the algorithm uses constant extra space.

    if not arr:
        return -1  # Return -1 for an empty array

    if len(arr) == 1:
        return 0  # If array contains only one element, no rotations

    low, high = 0, len(arr) - 1  # Initialize pointers

    while low <= high:
        mid = (low + high) // 2  # Calculate mid index

        # Check if mid is the point of rotation
        if mid > 0 and arr[mid - 1] > arr[mid]:
            return mid

        # Check if the left part is sorted
        if arr[low] <= arr[mid]:
            # If the entire segment is sorted, no rotation in this segment
            if arr[low] <= arr[high]:
                return low
            # Otherwise, search in the right half
            low = mid + 1
        else:
            # Search in the left half
            high = mid - 1

    return -1  # No rotation found

# Example test cases
tests = [
    {
        "input": {"arr": [5, 6, 9, 10, 1, 2, 3, 4]},
        "output": 4
    },
    {
        "input": {"arr": [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 4]},
        "output": 6
    },
    {
        "input": {"arr": [5, 6, 9, 9, 0, 2, 3, 4]},
        "output": 4
    },
    {
        "input": {"arr": [5]},
        "output": 0
    },
    {
        "input": {"arr": [5, 6, 9, 10, 0, 2, 3, 4]},
        "output": 4
    },
    {
        "input": {"arr": []},
        "output": -1
    },
    {
        "input": {"arr": [0, 2, 3, 4, 5, 7, 8]},
        "output": 0
    },
]

# Test the function with provided test cases
for test in tests:
    print(cal_rotations(**test["input"]) == test["output"])
