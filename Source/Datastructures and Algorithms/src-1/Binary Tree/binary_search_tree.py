from collections import deque

# Class representing a node in the binary tree
class Node:
    def __init__(self, key):
        # Initialize node with a value and left/right child pointers
        self.left = None
        self.right = None
        self.value = key

# Class for Binary Tree structure and operations
class BinaryTree:
    def __init__(self):
        # Initialize the binary tree with an empty root
        self.root = None

    # Insert a new value into the binary tree
    def insert(self, value):
        if self.root is None:
            # If the tree is empty, set the root node
            self.root = Node(value)
        else:
            # Recursively insert the value into the appropriate position
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                # Insert value to the left if it's smaller and no left child exists
                current.left = Node(value)
            else:
                # Recur down the left subtree
                self._insert(current.left, value)
        else:
            if current.right is None:
                # Insert value to the right if it's larger and no right child exists
                current.right = Node(value)
            else:
                # Recur down the right subtree
                self._insert(current.right, value)

    # In-order traversal of the tree (Left, Root, Right)
    def in_order(self):
        return self._in_order(self.root, [])

    def _in_order(self, node, nodes):
        if node:
            # Traverse the left subtree
            self._in_order(node.left, nodes)
            # Visit the root
            nodes.append(node.value)
            # Traverse the right subtree
            self._in_order(node.right, nodes)
        return nodes

    # Pre-order traversal of the tree (Root, Left, Right)
    def pre_order(self):
        return self._pre_order(self.root, [])

    def _pre_order(self, node, nodes):
        if node:
            # Visit the root
            nodes.append(node.value)
            # Traverse the left subtree
            self._pre_order(node.left, nodes)
            # Traverse the right subtree
            self._pre_order(node.right, nodes)
        return nodes

    # Post-order traversal of the tree (Left, Right, Root)
    def post_order(self):
        return self._post_order(self.root, [])

    def _post_order(self, node, nodes):
        if node:
            # Traverse the left subtree
            self._post_order(node.left, nodes)
            # Traverse the right subtree
            self._post_order(node.right, nodes)
            # Visit the root
            nodes.append(node.value)
        return nodes

    # Search for a value in the binary tree
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        # Search in the left subtree if the value is smaller
        if value < node.value:
            return self._search(node.left, value)
        # Search in the right subtree if the value is larger
        else:
            return self._search(node.right, value)

    # Find the minimum value in the tree
    def _find_min(self, node):
        if node is None:
            return None
        # Traverse to the leftmost node (smallest value)
        while node.left is not None:
            node = node.left
        return node.value

    def find_min(self):
        return self._find_min(self.root)

    # Find the maximum value in the tree
    def _find_max(self, node):
        if node is None:
            return None
        # Traverse to the rightmost node (largest value)
        while node.right is not None:
            node = node.right
        return node.value

    def find_max(self):
        return self._find_max(self.root)

    # Find the height of the binary tree
    def _find_height(self, node):
        if node is None:
            return -1
        # Recursively find the height of left and right subtrees and add 1
        left = self._find_height(node.left)
        right = self._find_height(node.right)
        return 1 + max(left, right)

    def find_height(self):
        return self._find_height(self.root)

    # Breadth-first search (BFS) traversal
    def bfs(self):
        if self.root is None:
            return []

        # Initialize queue and result list
        queue = deque([self.root])
        nodes = []

        # Traverse level by level
        while queue:
            node = queue.popleft()
            nodes.append(node.value)

            # Add left and right children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return nodes

    # Delete a value from the binary tree
    def _delete(self, node, value):
        if node is None:
            return node

        if value < node.value:
            # Recur into the left subtree
            node.left = self._delete(node.left, value)
        elif value > node.value:
            # Recur into the right subtree
            node.right = self._delete(node.right, value)
        else:
            # Node to be deleted found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Find the smallest node in the right subtree
            min_larger_node_value = self._find_min(node.right)
            node.value = min_larger_node_value
            # Delete the duplicate node
            node.right = self._delete(node.right, min_larger_node_value)
        return node

    def delete(self, value):
        self.root = self._delete(self.root, value)

    # Count the total number of nodes in the tree
    def _count_nodes(self, node):
        if node is None:
            return 0
        # Recursively count left and right subtrees, then add 1 for the current node
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def count_nodes(self):
        return self._count_nodes(self.root)

    # Calculate the diameter of the tree
    def diameter(self):
        self.dim = 0
        return self._diameter(self.root)

    def _diameter(self, node):
        if node is None:
            return 0

        left = self._diameter(node.left)
        right = self._diameter(node.right)

        # Update the diameter
        self.dim = max(self.dim, left + right)

        return 1 + max(left, right)

    # Check if the binary tree is balanced
    def isBalanced(self):
        return self._isBalanced(self.root)

    def _isBalanced(self, node):
        if node is None:
            return (True, -1)

        # Recursively check if left and right subtrees are balanced
        left_balanced, left_height = self._isBalanced(node.left)
        right_balanced, right_height = self._isBalanced(node.right)

        # Check if the current node is balanced
        current_balance = (left_balanced and right_balanced and abs(left_height - right_height) <= 1)
        current_height = max(left_height, right_height) + 1

        return current_balance, current_height

# Example usage of BinaryTree
# Initialize the BinaryTree instance
tree = BinaryTree()

# Test find_height on an empty tree
print("Height of empty tree:", tree.find_height())  # Expected: -1

# Insert nodes and test height increment
tree.insert(5)
print("Height after inserting 5:", tree.find_height())  # Expected: 0

tree.insert(55)
print("Height after inserting 55:", tree.find_height())  # Expected: 1

tree.insert(15)
print("Height after inserting 15:", tree.find_height())  # Expected: 2

# Insert more nodes
tree.insert(7)
tree.insert(17)
tree.insert(458)
print(tree.isBalanced())

print(tree.diameter())

# Test the search function
print("Searching for 45:", tree.search(45))  # Expected: False
print("Searching for 5:", tree.search(5))    # Expected: True
print("Searching for 458:", tree.search(458)) # Expected: True

# Test the find_min and find_max functions
print("Minimum value in the tree:", tree.find_min())  # Expected: 5
print("Maximum value in the tree:", tree.find_max())  # Expected: 458

# Test BFS traversal
print("BFS Traversal:", tree.bfs())  # Expected: [5, 55, 15, 7, 17, 458]

# Test Pre-order, Post-order, and In-order traversals
print("Pre-order traversal:", tree.pre_order())   # Expected: [5, 55, 15, 7, 17, 458]
print("Post-order traversal:", tree.post_order()) # Expected: [7, 17, 15, 458, 55, 5]
print("In-order traversal:", tree.in_order())     # Expected: [5, 7, 15, 17, 55, 458]

# Test the count_nodes function
print("Total nodes in the tree:", tree.count_nodes())  # Expected: 6

# Test delete function
tree.delete(15)  # Deleting a node with two children
print("In-order traversal after deleting 15:", tree.bfs())  # Expected: [7, 17, 55, 458]

print(tree.diameter())
print(tree.isBalanced())
