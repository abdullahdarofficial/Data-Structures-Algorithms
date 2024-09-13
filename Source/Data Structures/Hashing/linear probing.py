class LinearHashing:
    def __init__(self, initial_size=4):
        # Time Complexity: O(n), where n is the initial size of the table.
        # Initializes the hash table with empty buckets (lists) for each index.
        self.size = initial_size  # Initial size of the hash table
        self.table = [[] for _ in range(self.size)]  # Create empty lists (buckets) for each index
        self.next_split_index = 0  # Track the next bucket to split during resizing
        self.current_level = 0  # Track the current level of hashing (expands as resizing occurs)

    def _hash(self, key, level=None):
        """
        Primary hash function based on modulus.

        Time Complexity: O(1)
        """
        if level is None:  # If level is not specified, use the current level
            level = self.current_level
        # Return the modulus of the key to determine its index
        return key % (self.size * 2 ** level)

    def _resize(self):
        """
        Resize the table by splitting buckets when needed.

        Time Complexity: O(n), where n is the current size of the table.
        This process involves redistributing all keys from the current table.
        """
        # Double the size of the table (new size)
        new_size = self.size * 2
        new_table = [[] for _ in range(new_size)]  # Create a new table with double the size

        # Rehash and redistribute all keys from the old table
        for i in range(self.size):
            for key, value in self.table[i]:
                # Recalculate the new index based on the new level
                new_index = self._hash(key, self.current_level + 1) % new_size
                new_table[new_index].append((key, value))  # Reinsert into the new table

        self.table = new_table  # Replace old table with the new one
        self.size = new_size  # Update the table size
        self.current_level += 1  # Move to the next hashing level

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.

        Time Complexity:
        - Best case: O(1), when no resizing is triggered.
        - Worst case: O(n), if resizing is triggered (rehashing and redistributing keys).
        """
        index = self._hash(key)  # Compute the hash index (O(1))
        bucket_index = index % self.size  # Find the appropriate bucket

        bucket = self.table[bucket_index]  # Retrieve the bucket at the computed index
        if len(bucket) >= 4:  # If the bucket size reaches threshold, trigger resizing
            self._resize()  # Resizing and rehashing (O(n))
            index = self._hash(key)  # Recalculate index after resizing (O(1))
            bucket_index = index % self.size  # Get the new bucket index (O(1))
            bucket = self.table[bucket_index]  # Get the updated bucket (O(1))

        # Search for the key in the bucket and update if it already exists
        for i, (k, v) in enumerate(bucket):  # O(b), where b is the bucket size (typically small)
            if k == key:
                bucket[i] = (key, value)  # Update the value if the key already exists (O(1))
                return

        # Append new key-value pair if key does not exist in the bucket
        bucket.append((key, value))  # O(1) to append a new element

    def search(self, key):
        """
        Search for a key in the hash table and return its value.

        Time Complexity:
        - Best case: O(1), when the key is found in the first lookup.
        - Worst case: O(b), where b is the bucket size. Typically, the bucket size is small.
        """
        index = self._hash(key)  # Compute the hash index (O(1))
        bucket_index = index % self.size  # Find the appropriate bucket (O(1))

        # Search the bucket for the key
        for k, v in self.table[bucket_index]:  # O(b), where b is the bucket size
            if k == key:
                return v  # Return the value if the key is found (O(1))

        return None  # Return None if the key is not found (O(1))

    def delete(self, key):
        """
        Delete a key from the hash table.

        Time Complexity:
        - Best case: O(1), when the key is found and deleted in the first lookup.
        - Worst case: O(b), where b is the bucket size. Typically, the bucket size is small.
        """
        index = self._hash(key)  # Compute the hash index (O(1))
        bucket_index = index % self.size  # Find the appropriate bucket (O(1))

        bucket = self.table[bucket_index]  # Retrieve the bucket at the index (O(1))
        for i, (k, v) in enumerate(bucket):  # O(b), where b is the bucket size
            if k == key:
                del bucket[i]  # Delete the key-value pair (O(1))
                return

# Example usage
hash_table = LinearHashing()  # Initialize hash table with initial size 4

# Insert key-value pairs (some may trigger resizing)
hash_table.insert(10, "Value for 10")  # O(1)
hash_table.insert(20, "Value for 20")  # O(1)
hash_table.insert(30, "Value for 30")  # O(1)
hash_table.insert(40, "Value for 40")  # O(1)
hash_table.insert(50, "Value for 50")  # Triggers resizing, O(n)

# Search for keys (O(1) in the best case, O(b) in the worst case)
print("Search for 10:", hash_table.search(10))  # Output: Value for 10, O(1)
print("Search for 20:", hash_table.search(20))  # Output: Value for 20, O(1)
print("Search for 30:", hash_table.search(30))  # Output: Value for 30, O(1)
print("Search for 40:", hash_table.search(40))  # Output: Value for 40, O(1)
print("Search for 50:", hash_table.search(50))  # Output: Value for 50, O(1)
print("Search for 60:", hash_table.search(60))  # Output: None, O(1)

# Delete a key (O(1) in the best case, O(b) in the worst case)
hash_table.delete(20)
print("Search for 20 after deletion:", hash_table.search(20))  # Output: None, O(1)
