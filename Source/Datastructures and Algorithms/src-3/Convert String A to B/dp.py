def can_transform(source: str, target: str) -> int:
    s1 = len(source)
    s2 = len(target)

    # Initialize the table with dimensions (s1 + 1) x (s2 + 1)
    table = [[0 for _ in range(s2 + 1)] for _ in range(s1 + 1)]

    # Base cases: transforming empty source to target and vice versa
    for i in range(s1 + 1):
        table[i][0] = i  # Deleting all characters from source to match empty target
    for j in range(s2 + 1):
        table[0][j] = j  # Inserting all characters into empty source to match target

    # Fill the table
    for i in range(1, s1 + 1):
        for j in range(1, s2 + 1):
            if source[i - 1] == target[j - 1]:
                table[i][j] = table[i - 1][j - 1]  # No operation needed
            else:
                table[i][j] = min(
                    table[i - 1][j] + 1,  # Deletion a char from source string
                    table[i][j - 1] + 1,  # Insertion a character from source string
                    table[i - 1][j - 1] + 1  # Substitution a character from source string
                )
    for x in table:
        print(x)
    return table[s1][s2]

# Test cases
test_cases = [
    {"input": ("abc", "abd"), "expected": 1},
    {"input": ("abc", "ab"), "expected": 1},
    {"input": ("abc", "abcd"), "expected": 1},
    {"input": ("abc", "xyz"), "expected": 3},
    {"input": ("hello", "hell"), "expected": 1},
    {"input": ("python", "java"), "expected": 6},
    {"input": ("a", "ab"), "expected": 1},
    {"input": ("test", "tests"), "expected": 1},
    {"input": ("same", "same"), "expected": 0},
    {"input": ("", ""), "expected": 0},
    {"input": ("", "nonempty"), "expected": 8},
    {"input": ("nonempty", ""), "expected": 8},
]

# Running test cases
for i, test_case in enumerate(test_cases):
    inp = test_case["input"]
    expected = test_case["expected"]
    result = can_transform(*inp)
    assert result == expected, f"Test case {i+1} failed: input({inp}) => output({result}), expected({expected})"

print("All test cases passed!")
