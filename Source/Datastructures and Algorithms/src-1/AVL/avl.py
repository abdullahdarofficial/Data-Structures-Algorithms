class Node:
    def __init__(self, key):
        # Time Complexity: O(1) for node initialization
        self.key = key  # The key value for the node
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child
        self.height = 1  # Height of the node, initially 1

class AVLTree:
    def __init__(self):
        # Time Complexity: O(1) for initializing an empty tree
        self.root = None  # Root of the AVL tree

    def insert(self, root, key):
        """
        Insert a key into the subtree rooted at `root` and balance the tree.

        Time Complexity:
        - Best case: O(log n), when the tree is balanced.
        - Worst case: O(log n), the height of the tree in AVL is log n.
        """
        # Step 1: Perform normal BST insert
        if not root:
            return Node(key)  # Insert new node if root is None
        elif key < root.key:
            root.left = self.insert(root.left, key)  # Recur for left subtree
        else:
            root.right = self.insert(root.right, key)  # Recur for right subtree

        # Step 2: Update the height of this ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))  # O(1)

        # Step 3: Get the balance factor to check if this node became unbalanced
        balance = self.get_balance(root)  # O(1)

        # Step 4: If unbalanced, there are 4 possible cases

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)  # O(1)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)  # O(1)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)  # First perform left rotate (O(1))
            return self.right_rotate(root)  # Then right rotate (O(1))

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)  # First perform right rotate (O(1))
            return self.left_rotate(root)  # Then left rotate (O(1))

        return root  # Return the (potentially balanced) root

    def left_rotate(self, z):
        """
        Perform a left rotation on the subtree rooted at `z`.
        Time Complexity: O(1)
        """
        y = z.right  # `y` becomes the new root
        T2 = y.left  # `T2` is the left subtree of `y`

        # Perform rotation
        y.left = z  # Move `z` to be the left child of `y`
        z.right = T2  # Update `z`'s right subtree

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))  # O(1)
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))  # O(1)

        # Return new root
        return y  # `y` becomes the new root

    def right_rotate(self, z):
        """
        Perform a right rotation on the subtree rooted at `z`.
        Time Complexity: O(1)
        """
        y = z.left  # `y` becomes the new root
        T3 = y.right  # `T3` is the right subtree of `y`

        # Perform rotation
        y.right = z  # Move `z` to be the right child of `y`
        z.left = T3  # Update `z`'s left subtree

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))  # O(1)
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))  # O(1)

        # Return new root
        return y  # `y` becomes the new root

    def get_height(self, node):
        """
        Get the height of the node.
        Time Complexity: O(1)
        """
        if not node:
            return 0
        return node.height  # Return the height of the node

    def get_balance(self, node):
        """
        Get the balance factor of the node.
        Time Complexity: O(1)
        """
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)  # Calculate balance factor

    def pre_order(self, root):
        """
        Perform a pre-order traversal of the tree.
        Time Complexity: O(n), where n is the number of nodes in the tree.
        """
        if not root:
            return
        print("{0} ".format(root.key), end="")  # Print root key
        self.pre_order(root.left)  # Recur on the left subtree
        self.pre_order(root.right)  # Recur on the right subtree

    def insert_node(self, key):
        """
        Wrapper to insert a node into the tree.
        Time Complexity: Same as the `insert` function, O(log n) in the average and worst case.
        """
        self.root = self.insert(self.root, key)  # Insert node into the tree

# Usage example
avl_tree = AVLTree()

# Inserting nodes
nodes = [10, 20, 30, 40, 50, 25]
for node in nodes:
    avl_tree.insert_node(node)

# Pre-order traversal of the AVL tree
print("Pre-order traversal of the AVL tree:")
avl_tree.pre_order(avl_tree.root)  # O(n)
