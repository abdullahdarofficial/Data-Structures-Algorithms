import heapq
from collections import Counter, defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char  # The character represented by this node (None for internal nodes)
        self.freq = freq  # Frequency of the character
        self.left = None  # Left child (for '0' bit in Huffman encoding)
        self.right = None  # Right child (for '1' bit in Huffman encoding)

    # Define the comparison operation for heapq (min-heap)
    def __lt__(self, other):
        return self.freq < other.freq  # Compare nodes based on frequency

def build_huffman_tree(text):
    """
    Build a Huffman tree from the input text.
    :param text: The input string
    :return: The root of the Huffman tree
    """
    # Count the frequency of each character in the text
    # Time complexity: O(n), where n is the length of the input text
    frequency = Counter(text)  # Creates a frequency dictionary {char: freq}

    # Create a priority queue (min-heap) with nodes for each character
    # Time complexity: O(d log d), where d is the number of distinct characters in the text
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)  # Convert the list into a heap (min-heap)

    # Build the Huffman Tree
    # Time complexity: O(d log d), as we combine nodes in the heap
    while len(priority_queue) > 1:
        # Extract the two nodes with the lowest frequencies
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        # Merge the two nodes into a new internal node
        merged = Node(None, left.freq + right.freq)
        merged.left = left  # Left child of the merged node
        merged.right = right  # Right child of the merged node
        # Add the merged node back to the heap
        heapq.heappush(priority_queue, merged)

    # The final node in the heap is the root of the Huffman tree
    return priority_queue[0]

def generate_codes(root):
    """
    Generate Huffman codes for each character based on the Huffman tree.
    :param root: The root of the Huffman tree
    :return: A dictionary of Huffman codes for each character
    """
    # Helper function to recursively generate the Huffman codes
    def _generate_codes(node, current_code):
        if node is None:
            return {}
        if node.char is not None:  # Leaf node (contains a character)
            return {node.char: current_code}  # Return the code for this character
        codes = {}
        # Recur for the left child (add '0' to the current code)
        codes.update(_generate_codes(node.left, current_code + '0'))
        # Recur for the right child (add '1' to the current code)
        codes.update(_generate_codes(node.right, current_code + '1'))
        return codes

    # Call the helper function to generate codes starting from the root
    return _generate_codes(root, '')

def huffman_encoding(text):
    """
    Encode the input text using Huffman encoding.
    :param text: The input string
    :return: The encoded string and the corresponding Huffman codes
    """
    if not text:
        return "", None  # If the input text is empty, return empty results

    # Build the Huffman tree for the input text
    root = build_huffman_tree(text)

    # Generate the Huffman codes for each character
    codes = generate_codes(root)

    # Encode the input text using the generated Huffman codes
    # Time complexity: O(n), where n is the length of the input text
    encoded_text = ''.join(codes[char] for char in text)

    return encoded_text, codes

def huffman_decoding(encoded_text, codes):
    """
    Decode the encoded text using Huffman codes.
    :param encoded_text: The encoded string
    :param codes: The dictionary of Huffman codes
    :return: The decoded original string
    """
    # Create a reverse mapping of the Huffman codes to characters
    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ''
    decoded_text = []

    # Iterate over the encoded bits and decode the characters
    # Time complexity: O(m), where m is the length of the encoded text
    for bit in encoded_text:
        current_code += bit  # Accumulate bits for the current code
        if current_code in reverse_codes:  # If the code matches a character
            decoded_text.append(reverse_codes[current_code])  # Add the character to the decoded text
            current_code = ''  # Reset the current code for the next character

    return ''.join(decoded_text)  # Return the decoded string

# Example usage
text = "this is an example for huffman encoding"

# Encode the text using Huffman encoding
encoded_text, codes = huffman_encoding(text)
print("Encoded text:", encoded_text)
print("Huffman Codes:", codes)

# Decode the encoded text back to the original
decoded_text = huffman_decoding(encoded_text, codes)
print("Decoded text:", decoded_text)

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Building the Huffman Tree:
#    - Time complexity: O(n + d log d), where n is the length of the input text, and d is the number of distinct characters.
#    - Counting the frequencies takes O(n), and building the heap and the tree takes O(d log d).

# 2. Generating Huffman codes:
#    - Time complexity: O(d), where d is the number of distinct characters.
#    - We recursively traverse the tree once to generate the codes.

# 3. Encoding the text:
#    - Time complexity: O(n), where n is the length of the input text.
#    - We replace each character with its corresponding Huffman code.

# 4. Decoding the encoded text:
#    - Time complexity: O(m), where m is the length of the encoded text.
#    - We traverse the encoded string and map each bit sequence back to the corresponding character.

# Overall time complexity:
# - Best-case time complexity: O(n + d log d), where n is the length of the text and d is the number of distinct characters.
# - Average-case time complexity: O(n + d log d).
# - Worst-case time complexity: O(n + d log d), since building the Huffman tree dominates the complexity.

# Space complexity:
# - Space complexity: O(d), where d is the number of distinct characters, since we store the Huffman tree and the codes.
