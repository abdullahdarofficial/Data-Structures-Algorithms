def check_subarray_sum(arr, target):

    size = len(arr)
    for i in range(size):
        sum = 0
        for j in range(i, size):
            sum += arr[j]
            if sum == target:
                return True
    return False  # Replace with actual logic

if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 4, 20, 3, 10, 5]
    target1 = 33
    print("Test Case 1:", check_subarray_sum(arr1, target1))  # Expected: True

    # Test Case 2
    arr2 = [10, 2, -2, -20, 10]
    target2 = -10
    print("Test Case 2:", check_subarray_sum(arr2, target2))  # Expected: True

    # Test Case 3
    arr3 = [-10, 0, 2, -2, 5, 3]
    target3 = 5
    print("Test Case 3:", check_subarray_sum(arr3, target3))  # Expected: True

    # Test Case 4
    arr4 = [1, 2, 3, 7, 5]
    target4 = 12
    print("Test Case 4:", check_subarray_sum(arr4, target4))  # Expected: True

    # Test Case 5
    arr5 = [1, 2, 3, 4, 5]
    target5 = 15
    print("Test Case 5:", check_subarray_sum(arr5, target5))  # Expected: True

    # Test Case 6
    arr6 = [1, 2, 3, 8, 9]
    target6 = 15
    print("Test Case 6:", check_subarray_sum(arr6, target6))  # Expected: False
