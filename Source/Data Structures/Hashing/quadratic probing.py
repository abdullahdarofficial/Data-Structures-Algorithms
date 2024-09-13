class QuadraticProbingHashTable:
    def __init__(self, size):
        # Time Complexity: O(n), where n is the size of the table.
        # Initializes the hash table with `None` values for empty slots.
        self.size = size  # Size of the hash table
        self.table = [None] * size  # Initialize hash table with None
        self.EMPTY = object()  # Sentinel value for deleted slots
        self.DELETED = object()  # Sentinel value for deleted slots (used to mark deleted items)

    def _hash(self, key):
        """
        Basic hash function using modulo operation.

        Time Complexity: O(1)
        """
        return key % self.size  # Simple modulus to get hash index

    def _probe(self, key, i):
        """
        Quadratic probing function to handle collisions.

        Time Complexity: O(1)
        """
        # Quadratic probing formula: (hash(key) + i^2) % size
        return (self._hash(key) + i * i) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table using quadratic probing.

        Time Complexity:
        - Best case: O(1), when no collision occurs.
        - Worst case: O(n), where n is the size of the table if many collisions occur and all slots are probed.
        """
        for i in range(self.size):  # Iterate over the table with quadratic probing
            index = self._probe(key, i)  # Calculate the index using quadratic probing (O(1))
            if self.table[index] is None or self.table[index] == self.EMPTY:  # Check if the slot is empty or marked as deleted
                self.table[index] = (key, value)  # Insert the key-value pair (O(1))
                return
            if self.table[index][0] == key:  # If the key already exists, update its value
                self.table[index] = (key, value)  # Update value (O(1))
                return
        # If the table is full, raise an exception
        raise Exception("Hash table is full")  # Worst case: O(n)

    def search(self, key):
        """
        Search for a key in the hash table and return its value.

        Time Complexity:
        - Best case: O(1), when the key is found in the first probe.
        - Worst case: O(n), where n is the size of the table if many collisions occur.
        """
        for i in range(self.size):  # Iterate over the table with quadratic probing
            index = self._probe(key, i)  # Calculate the index using quadratic probing (O(1))
            if self.table[index] is None:  # If we reach an empty slot, the key is not present
                return None  # Key not found (O(1))
            if self.table[index] == self.EMPTY:  # Skip deleted slots
                continue  # Continue probing (O(1))
            if self.table[index][0] == key:  # If the key is found
                return self.table[index][1]  # Return the associated value (O(1))
        return None  # Key not found after probing all slots (Worst case: O(n))

    def delete(self, key):
        """
        Delete a key from the hash table by marking its slot as EMPTY.

        Time Complexity:
        - Best case: O(1), when the key is found in the first probe.
        - Worst case: O(n), where n is the size of the table if many collisions occur.
        """
        for i in range(self.size):  # Iterate over the table with quadratic probing
            index = self._probe(key, i)  # Calculate the index using quadratic probing (O(1))
            if self.table[index] is None:  # If we reach an empty slot, the key is not present
                return  # Key not found (O(1))
            if self.table[index] == self.EMPTY:  # Skip deleted slots
                continue  # Continue probing (O(1))
            if self.table[index][0] == key:  # If the key is found
                self.table[index] = self.EMPTY  # Mark the slot as deleted (O(1))
                return

# Example usage
hash_table = QuadraticProbingHashTable(size=10)  # Initialize hash table with size 10

# Insert key-value pairs
hash_table.insert(10, "Value for 10")  # O(1)
hash_table.insert(20, "Value for 20")  # O(1)
hash_table.insert(30, "Value for 30")  # O(1)

# Search for keys
print("Search for 10:", hash_table.search(10))  # Output: Value for 10, O(1)
print("Search for 20:", hash_table.search(20))  # Output: Value for 20, O(1)
print("Search for 30:", hash_table.search(30))  # Output: Value for 30, O(1)
print("Search for 40:", hash_table.search(40))  # Output: None, O(n) in the worst case

# Delete a key
hash_table.delete(20)  # O(1)
print("Search for 20 after deletion:", hash_table.search(20))  # Output: None, O(1)
