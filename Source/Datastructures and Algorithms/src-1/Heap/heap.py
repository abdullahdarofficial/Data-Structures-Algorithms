import heapq

# Class for Min-Heap implementation
class MinHeap:
    def __init__(self):
        # Time Complexity: O(1)
        # Initialize an empty list to represent the heap
        self.heap = []

    # Method to insert an item into the heap
    def push(self, item):
        # Time Complexity: O(log n), where n is the number of elements in the heap
        # Add item to the heap and maintain heap property
        heapq.heappush(self.heap, item)

    # Method to remove and return the smallest item from the heap
    def pop(self):
        # Time Complexity: O(log n), where n is the number of elements in the heap
        if self.heap:
            # Remove the smallest item (root of the heap)
            return heapq.heappop(self.heap)
        # Raise an error if the heap is empty
        raise IndexError("pop from an empty heap")

    # Method to get the smallest item without removing it
    def peek(self):
        # Time Complexity: O(1)
        if self.heap:
            # Return the smallest item (root of the heap)
            return self.heap[0]
        # Raise an error if the heap is empty
        raise IndexError("peek from an empty heap")

    # Method to display the heap
    def display(self):
        # Time Complexity: O(n), where n is the number of elements in the heap
        print("Min-Heap:", self.heap)

# Class for Max-Heap implementation
class MaxHeap:
    def __init__(self):
        # Time Complexity: O(1)
        # Initialize an empty list to represent the heap
        self.heap = []

    # Method to insert an item into the heap
    def push(self, item):
        # Time Complexity: O(log n), where n is the number of elements in the heap
        # Add item as a negative value to simulate max-heap
        heapq.heappush(self.heap, -item)

    # Method to remove and return the largest item from the heap
    def pop(self):
        # Time Complexity: O(log n), where n is the number of elements in the heap
        if self.heap:
            # Remove the largest item by popping the smallest negative value
            return -heapq.heappop(self.heap)
        # Raise an error if the heap is empty
        raise IndexError("pop from an empty heap")

    # Method to get the largest item without removing it
    def peek(self):
        # Time Complexity: O(1)
        if self.heap:
            # Return the largest item by accessing the smallest negative value
            return -self.heap[0]
        # Raise an error if the heap is empty
        raise IndexError("peek from an empty heap")

    # Method to display the heap
    def display(self):
        # Time Complexity: O(n), where n is the number of elements in the heap
        # Convert the negative values back to positive for display
        print("Max-Heap:", [-item for item in self.heap])

# Example Usage
if __name__ == "__main__":
    # Min-Heap Example
    min_heap = MinHeap()
    min_heap.push(5)
    min_heap.push(3)
    min_heap.push(8)
    min_heap.push(1)

    print("Min-Heap Operations:")
    min_heap.display()  # Display the current state of the min-heap
    print("Peek:", min_heap.peek())  # Show the smallest item
    print("Pop:", min_heap.pop())  # Remove and return the smallest item
    min_heap.display()  # Display the heap after popping the smallest item

    # Max-Heap Example
    max_heap = MaxHeap()
    max_heap.push(5)
    max_heap.push(3)
    max_heap.push(8)
    max_heap.push(1)

    print("\nMax-Heap Operations:")
    max_heap.display()  # Display the current state of the max-heap
    print("Peek:", max_heap.peek())  # Show the largest item
    print("Pop:", max_heap.pop())  # Remove and return the largest item
    max_heap.display()  # Display the heap after popping the largest item
