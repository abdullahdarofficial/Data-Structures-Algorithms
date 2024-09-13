def bucket_sort(arr):
    # Create n empty buckets where n is the length of the array
    # Time complexity: O(n), where n is the length of the input array
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]  # Create 'num_buckets' empty buckets

    # Place elements into buckets based on value
    # Time complexity: O(n), as we iterate over the input array to place elements in buckets
    for num in arr:
        # Map each element to a bucket index, assuming numbers are in the range [0, 1)
        # Multiplying num by num_buckets ensures that elements are distributed across the buckets
        bucket_index = int(num * num_buckets)
        buckets[bucket_index].append(num)  # Append the number to the corresponding bucket

    # Sort individual buckets
    # Time complexity: O(k * log k) for each bucket, where k is the number of elements in a bucket.
    # In the best case, the number of elements per bucket is small, so sorting is nearly O(1).
    for bucket in buckets:
        bucket.sort()  # Sort each bucket (typically using Timsort, which is O(k * log k))

    # Concatenate sorted buckets into a single array
    # Time complexity: O(n), as we concatenate the sorted buckets into the final array
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)  # Extend the sorted array with the sorted bucket

    return sorted_arr  # Return the final sorted array

# Example usage
arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Creating buckets:
#    - Time complexity: O(n), as we create 'n' empty buckets.
#    - Best, Average, and Worst-case: O(n), where n is the number of elements in the input array.

# 2. Distributing elements into buckets:
#    - Time complexity: O(n), as we iterate through the input array once to distribute the elements into buckets.
#    - Best, Average, and Worst-case: O(n).

# 3. Sorting each individual bucket:
#    - Time complexity depends on how elements are distributed:
#      - If elements are distributed uniformly, each bucket contains around n/k elements (where k is the number of buckets).
#      - Sorting each bucket takes O(k * log k) time, but since there are k buckets, sorting across all buckets will take approximately O(n * log(n/k)).
#    - Best-case time complexity: O(n) (if the elements are already uniformly distributed, and each bucket has a small number of elements).
#    - Average-case time complexity: O(n + n * log(n/k)) ≈ O(n) for uniform distribution and constant bucket size.
#    - Worst-case time complexity: O(n^2) (if all elements fall into one bucket, essentially reducing the algorithm to O(n^2) for sorting).

# 4. Concatenating sorted buckets:
#    - Time complexity: O(n), as we iterate through each sorted bucket and append the elements to the final result array.
#    - Best, Average, and Worst-case: O(n).

# Overall time complexity:
# - Best-case time complexity: O(n) (for uniformly distributed input where each bucket has few elements).
# - Average-case time complexity: O(n + n * log(n/k)) ≈ O(n) (assuming uniform distribution of elements).
# - Worst-case time complexity: O(n^2) (if all elements fall into one bucket, leading to inefficient sorting).

