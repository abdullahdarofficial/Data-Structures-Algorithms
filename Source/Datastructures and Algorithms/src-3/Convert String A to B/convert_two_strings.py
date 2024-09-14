
def can_transform(source: str, target: str) -> int:
    s1 = len(source)
    s2 = len(target)

    def recursive(idx1=0, idx2=0):
        # Base cases
        if idx1 == s1:
            return s2 - idx2  # Remaining characters in target
        if idx2 == s2:
            return s1 - idx1  # Remaining characters in source
        # If characters match, move both indices
        if source[idx1] == target[idx2]:
            return recursive(idx1 + 1, idx2 + 1)
        else:
            # Try all possible operations: Add, Drop, Update
            return min(
                1 + recursive(idx1 + 1, idx2),      # Drop from source
                1 + recursive(idx1, idx2 + 1),      # Add to source
                1 + recursive(idx1 + 1, idx2 + 1)   # Update source
            )

    # Calculate the minimum number of operations needed
    return recursive()

# Test cases
test_cases = [
    # Test Case 1
    {
        "input": ("abc", "abd"),
        "expected": 1
    },
    # Test Case 2
    {
        "input": ("abc", "ab"),
        "expected": 1
    },
    # Test Case 3
    {
        "input": ("abc", "abcd"),
        "expected": 1
    },
    # Test Case 4
    {
        "input": ("abc", "xyz"),
        "expected": 3
    },
    # Test Case 5
    {
        "input": ("hello", "hell"),
        "expected": 1
    },
    # Test Case 6
    {
        "input": ("python", "java"),
        "expected": 6
    },
    # Test Case 7
    {
        "input": ("a", "ab"),
        "expected": 1
    },
    # Test Case 8
    {
        "input": ("test", "tests"),
        "expected": 1
    },
    # Test Case 9: Same strings
    {
        "input": ("same", "same"),
        "expected": 0
    },
    # Test Case 10: Empty strings
    {
        "input": ("", ""),
        "expected": 0
    },
    # Test Case 11: Empty source, non-empty target
    {
        "input": ("", "nonempty"),
        "expected": 8
    },
    # Test Case 12: Non-empty source, empty target
    {
        "input": ("nonempty", ""),
        "expected": 8
    },
]

# Running test cases
for i, test_case in enumerate(test_cases):
    inp = test_case["input"]
    expected = test_case["expected"]
    result = can_transform(*inp)
    assert result == expected, f"Test case {i+1} failed: input({inp}) => output({result}), expected({expected})"

print("All test cases passed!")
