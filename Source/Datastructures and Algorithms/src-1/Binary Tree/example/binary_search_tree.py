from collections import deque

class Node:
    def __init__(self, key):
        # Time Complexity: O(1) for initializing a new node
        self.left = None  # Left child of the node
        self.right = None  # Right child of the node
        self.value = key  # Value of the node

class BinaryTree:
    def __init__(self):
        # Time Complexity: O(1) for initializing an empty tree
        self.root = None  # Root of the binary tree

    def insert(self, value):
        # Time Complexity: O(log n) in the best case, O(n) in the worst case (unbalanced tree)
        if self.root is None:
            self.root = Node(value)  # Insert the first node as the root
        else:
            self._insert(self.root, value)  # Recur to insert the value

    def _insert(self, current, value):
        # Recursive helper to insert a node in the binary tree
        if value < current.value:
            if current.left is None:
                current.left = Node(value)  # Insert to the left
            else:
                self._insert(current.left, value)  # Recur on the left subtree
        else:
            if current.right is None:
                current.right = Node(value)  # Insert to the right
            else:
                self._insert(current.right, value)  # Recur on the right subtree

    def in_order(self):
        # Time Complexity: O(n), where n is the number of nodes
        return self._in_order(self.root, [])

    def _in_order(self, node, nodes):
        # Recursive in-order traversal (Left, Root, Right)
        if node:
            self._in_order(node.left, nodes)
            nodes.append(node.value)
            self._in_order(node.right, nodes)
        return nodes

    def pre_order(self):
        # Time Complexity: O(n)
        return self._pre_order(self.root, [])

    def _pre_order(self, node, nodes):
        # Recursive pre-order traversal (Root, Left, Right)
        if node:
            nodes.append(node.value)
            self._pre_order(node.left, nodes)
            self._pre_order(node.right, nodes)
        return nodes

    def post_order(self):
        # Time Complexity: O(n)
        return self._post_order(self.root, [])

    def _post_order(self, node, nodes):
        # Recursive post-order traversal (Left, Right, Root)
        if node:
            self._post_order(node.left, nodes)
            self._post_order(node.right, nodes)
            nodes.append(node.value)
        return nodes

    def search(self, value):
        # Time Complexity: O(log n) in the best case, O(n) in the worst case
        return self._search(self.root, value)

    def _search(self, node, value):
        # Recursive search in the binary tree
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def _find_min(self, node):
        # Time Complexity: O(log n) in the best case, O(n) in the worst case (unbalanced tree)
        if node is None:
            return None
        while node.left is not None:
            node = node.left  # Traverse to the leftmost node
        return node.value  # Return the minimum value

    def find_min(self):
        # Find the minimum value in the tree
        return self._find_min(self.root)

    def _find_max(self, node):
        # Time Complexity: O(log n) in the best case, O(n) in the worst case (unbalanced tree)
        if node is None:
            return None
        while node.right is not None:
            node = node.right  # Traverse to the rightmost node
        return node.value  # Return the maximum value

    def find_max(self):
        # Find the maximum value in the tree
        return self._find_max(self.root)

    def _find_height(self, node):
        # Time Complexity: O(n), since height computation requires visiting all nodes
        if node is None:
            return -1  # Base case: height of empty subtree is -1
        left = self._find_height(node.left)
        right = self._find_height(node.right)
        return 1 + max(left, right)  # Height is 1 + max of left and right heights

    def find_height(self):
        # Find the height of the tree
        return self._find_height(self.root)

    def bfs(self):
        # Time Complexity: O(n), where n is the number of nodes
        if self.root is None:
            return []
        queue = deque([self.root])
        nodes = []
        while queue:
            node = queue.popleft()  # Dequeue the current node
            nodes.append(node.value)  # Process the node
            if node.left:
                queue.append(node.left)  # Enqueue left child
            if node.right:
                queue.append(node.right)  # Enqueue right child
        return nodes

    def _delete(self, node, value):
        # Time Complexity: O(log n) in the best case, O(n) in the worst case (unbalanced tree)
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete(node.left, value)  # Recur on the left subtree
        elif value > node.value:
            node.right = self._delete(node.right, value)  # Recur on the right subtree
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children: get the inorder successor
            min_larger_node_value = self._find_min(node.right)
            node.value = min_larger_node_value
            node.right = self._delete(node.right, min_larger_node_value)
        return node

    def delete(self, value):
        # Wrapper function to delete a node from the tree
        self.root = self._delete(self.root, value)

    def _count_nodes(self, node):
        # Time Complexity: O(n)
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def count_nodes(self):
        # Count the number of nodes in the tree
        return self._count_nodes(self.root)

    def diameter(self):
        # Time Complexity: O(n)
        dim = 0
        return self._diameter(self.root, dim)

    def _diameter(self, node, dim):
        # Recursive function to calculate the diameter of the tree
        if node is None:
            return 0
        left = self._diameter(node.left, dim)
        right = self._diameter(node.right, dim)
        dim = max(dim, left + right)  # Update maximum diameter
        return 1 + max(left, right)

    def isBalanced(self):
        # Time Complexity: O(n)
        return self._isBalanced(self.root)[0]

    def _isBalanced(self, node):
        # Recursive function to check if the tree is balanced
        if node is None:
            return (True, -1)  # Empty tree is balanced with height -1
        left_balanced, left_height = self._isBalanced(node.left)
        right_balanced, right_height = self._isBalanced(node.right)
        current_balance = (left_balanced and right_balanced and abs(left_height - right_height) <= 1)
        current_height = 1 + max(left_height, right_height)
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
print(tree.isBalanced())  # Expected: (True, height)

print(tree.diameter())  # Expected diameter of the tree

# Test the search function
print("Searching for 45:", tree.search(45))  # Expected: False
print("Searching for 5:", tree.search(5))    # Expected: True
print("Searching for 458:", tree.search(458)) # Expected: True

# Test the find_min and find_max functions
print("Minimum value in the tree:", tree.find_min())  # Expected: 5
print("Maximum value in the tree:", tree.find_max())  # Expected: 458

# Test BFS traversal
print("BFS Traversal:", tree.bfs())  # Expected: [5, 55, 15, 458, 7, 17]

# Test Pre-order, Post-order, and In-order traversals
print("Pre-order traversal:", tree.pre_order())   # Expected: [5, 55, 15, 7, 17, 458]
print("Post-order traversal:", tree.post_order()) # Expected: [7
