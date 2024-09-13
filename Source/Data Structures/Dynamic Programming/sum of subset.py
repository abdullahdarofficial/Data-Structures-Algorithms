def subset_sum(nums, target):
    """
    Determine if there is a subset of `nums` that sums up to `target`.

    :param nums: List of integers
    :param target: Target sum
    :return: True if a subset with the sum of `target` exists, False otherwise
    """
    n = len(nums)  # Number of elements in the list

    # Create a DP table with (n+1) rows and (target+1) columns initialized to False
    # dp[i][j] will be True if there is a subset of the first 'i' numbers that sums to 'j'
    # Time complexity: O(n * target), since we create a table with n+1 rows and target+1 columns
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # There is always a subset with sum 0 (empty subset), hence True for dp[i][0]
    # Time complexity: O(n), where n is the number of elements
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the DP table
    # Time complexity: O(n * target), where n is the number of elements and target is the sum
    for i in range(1, n + 1):  # Iterate over each number in nums
        for j in range(1, target + 1):  # Iterate over all possible sums from 1 to target
            if nums[i - 1] <= j:  # If the current number can be part of the sum
                # Either include the current number or exclude it
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                # Exclude the current number (it can't be part of the sum as it's greater than j)
                dp[i][j] = dp[i - 1][j]

    # The result is in the bottom-right cell of the DP table
    return dp[n][target]  # Return whether there is a subset that sums to 'target'

# Example usage
nums = [3, 34, 4, 12, 5, 2]
target = 9

# Call the function and print the result
result = subset_sum(nums, target)
print(f"Subset with sum {target} exists: {result}")

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Creating the DP table:
#    - Time complexity: O(n * target), where n is the number of elements in nums and target is the target sum.
#    - This involves creating a DP table with (n+1) rows and (target+1) columns.

# 2. Filling the DP table:
#    - Time complexity: O(n * target), as we iterate over each element and for each element,
#      we check all possible sums from 1 to the target.
#    - For each element, we make a decision to include it in the subset or not.

# Overall time complexity:
# - Best-case time complexity: O(n * target), as the table must be filled for all elements and sums.
# - Average-case time complexity: O(n * target).
# - Worst-case time complexity: O(n * target), since every element and sum combination is processed.

# Space complexity:
# - Space complexity: O(n * target), due to the space required for the DP table of size (n+1) x (target+1).
