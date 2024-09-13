import heapq

class DoubleHashingHashTable:
    def __init__(self, size):
        # Time Complexity: O(n), where n is the size of the hash table.
        # Initializes the hash table with None values.
        self.size = size  # Store the size of the hash table
        self.table = [None] * size  # Initialize table with None
        self.EMPTY = object()  # Sentinel value for empty slots
        self.DELETED = object()  # Sentinel value for deleted slots (not used directly here)

    def _hash1(self, key):
        # Time Complexity: O(1), constant time as it's just modulus operation.
        return key % self.size  # Primary hash function

    def _hash2(self, key):
        # Time Complexity: O(1), constant time as it's just modulus operation with additional arithmetic.
        return 1 + (key % (self.size - 1))  # Secondary hash function for probing

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.

        Time Complexity:
        Best case: O(1), when there is no collision and the element is inserted directly.
        Worst case: O(n), where n is the size of the table, if many collisions force probing through many slots.
        """
        index = self._hash1(key)  # Calculate the initial index using hash1 (O(1))
        step = self._hash2(key)  # Calculate step size using hash2 (O(1))

        # Probing through the table
        while self.table[index] not in (None, self.EMPTY):  # While current slot is not free
            if self.table[index][0] == key:  # If key already exists, update it
                # Time Complexity: O(1) for finding an existing key
                self.table[index] = (key, value)  # Update key-value pair
                return
            # Time Complexity: O(1) for the modulus operation and index calculation
            index = (index + step) % self.size  # Move to the next index using double hashing

        # Insert new key-value pair into the table
        # Time Complexity: O(1) for insertion into an available slot
        self.table[index] = (key, value)  # Insert new key-value pair

    def search(self, key):
        """
        Search for a key in the hash table.

        Time Complexity:
        Best case: O(1), when the key is found in the first calculated index.
        Worst case: O(n), where n is the size of the table, if there are many collisions and probes.
        """
        index = self._hash1(key)  # Calculate the initial index using hash1 (O(1))
        step = self._hash2(key)  # Calculate step size using hash2 (O(1))

        # Probing through the table
        while self.table[index] is not None:  # Loop until an empty slot is found (O(1) for each check)
            if self.table[index] == self.EMPTY:  # Skip over deleted slots
                # Time Complexity: O(1) for skipping EMPTY
                index = (index + step) % self.size  # Move to the next slot
                continue
            if self.table[index][0] == key:  # If key is found
                # Time Complexity: O(1) for key comparison and returning the value
                return self.table[index][1]  # Return the value associated with the key
            index = (index + step) % self.size  # Move to the next index (O(1))

        # Time Complexity: O(1) for returning None if the key is not found
        return None  # Key not found in the hash table

    def delete(self, key):
        """
        Delete a key from the hash table by marking its slot as EMPTY.

        Time Complexity:
        Best case: O(1), when the key is found in the first calculated index.
        Worst case: O(n), where n is the size of the table, if there are many collisions and probes.
        """
        index = self._hash1(key)  # Calculate the initial index using hash1 (O(1))
        step = self._hash2(key)  # Calculate step size using hash2 (O(1))

        # Probing through the table
        while self.table[index] is not None:  # Loop until an empty slot is found (O(1) for each check)
            if self.table[index] == self.EMPTY:  # Skip over deleted slots
                # Time Complexity: O(1) for skipping EMPTY slots
                index = (index + step) % self.size  # Move to the next slot
                continue
            if self.table[index][0] == key:  # If key is found
                # Time Complexity: O(1) for marking the slot as EMPTY
                self.table[index] = self.EMPTY  # Mark this slot as deleted
                return
            index = (index + step) % self.size  # Move to the next index (O(1))

# Example usage
hash_table = DoubleHashingHashTable(size=10)  # O(n) space complexity, where n is the size of the table

# Insertions (each has best-case O(1), worst-case O(n) complexity depending on collisions)
hash_table.insert(10, "Value for 10")
hash_table.insert(20, "Value for 20")
hash_table.insert(30, "Value for 30")

# Searches (each has best-case O(1), worst-case O(n) complexity depending on collisions)
print("Search for 10:", hash_table.search(10))  # O(1)
print("Search for 20:", hash_table.search(20))  # O(1)
print("Search for 30:", hash_table.search(30))  # O(1)
print("Search for 40:", hash_table.search(40))  # O(n) - Worst-case as it needs to probe

# Deletion (best-case O(1), worst-case O(n) complexity depending on collisions)
hash_table.delete(20)
print("Search for 20 after deletion:", hash_table.search(20))  # O(n) - Probing for deleted slot
