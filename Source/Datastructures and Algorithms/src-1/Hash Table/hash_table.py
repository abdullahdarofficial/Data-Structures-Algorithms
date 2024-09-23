class HashTable:
    def __init__(self, size=10):
        # Time Complexity: O(n) for initializing the hash table with None values
        # Initialize the hash table with a given size and set up the table with None values
        self.size = size
        self.table = [None] * self.size
        self.count = 0  # Keep track of the number of items in the hash table

    # Private method to compute the hash index for a given key
    def _hash(self, key):
        # Time Complexity: O(1)
        return hash(key) % self.size

    # Private method for handling collisions using linear probing
    def _linear_probe(self, index):
        # Time Complexity: O(n) in the worst case if the table is almost full
        original_index = index
        # Find the next available index in case of a collision
        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash Table is full")
        return index

    # Method to insert or update a key-value pair in the hash table
    def insert(self, key, value):
        # Time Complexity: O(1) in the best case, O(n) in the worst case due to linear probing
        index = self._hash(key)  # Compute the hash index

        if self.table[index] is None:
            # If the slot is empty, insert the key-value pair
            self.table[index] = (key, value)
        else:
            if self.table[index][0] == key:
                # If the key already exists, update its value
                self.table[index] = (key, value)
            else:
                # If there's a collision, find a new index using linear probing
                new_index = self._linear_probe(index)
                self.table[new_index] = (key, value)
        self.count += 1

    # Method to retrieve a value associated with a given key
    def get(self, key):
        # Time Complexity: O(1) in the best case, O(n) in the worst case due to collisions
        index = self._hash(key)  # Compute the hash index
        original_index = index

        # Search for the key in the table, handling potential collisions
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]  # Return the value if the key is found

            index = (index + 1) % self.size
            if index == original_index:
                break

        return None  # Return None if the key is not found

    # Method to delete a key-value pair from the hash table
    def delete(self, key):
        # Time Complexity: O(1) in the best case, O(n) in the worst case due to probing
        index = self._hash(key)  # Compute the hash index
        original_index = index

        # Search for the key in the table and remove it
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None  # Remove the key-value pair
                self._rehash()  # Rehash the table to prevent clustering
                return

            index = (index + 1) % self.size
            if index == original_index:
                break

    # Private method to rehash the entire table
    def _rehash(self):
        # Time Complexity: O(n) where n is the number of elements in the table
        old_table = self.table  # Store the current table
        self.table = [None] * self.size  # Create a new empty table
        self.count = 0  # Reset the count

        # Reinsert all non-None items from the old table into the new table
        for item in old_table:
            if item is not None:
                self.insert(item[0], item[1])

    # Method to display the current state of the hash table
    def display(self):
        # Time Complexity: O(n), where n is the size of the table
        for i in range(self.size):
            if self.table[i] is not None:
                print("index ", i, self.table[i])

# Example usage
if __name__ == "__main__":
    ht = HashTable(size=7)  # Hash table of size 7 for demonstration

    # Inserting key-value pairs
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("orange", 30)
    ht.insert("grapes", 40)
    ht.insert("melon", 50)

    ht.display()  # Display the hash table

    # Retrieving a value
    print(f"Value for 'banana': {ht.get('banana')}")  # Output: 20

    # Updating a value
    ht.insert("apple", 15)
    ht.display()

    # Deleting a key-value pair
    ht.delete("banana")
    ht.display()

    # Trying to delete a non-existent key
    ht.delete("cherry")
