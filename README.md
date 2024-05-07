# Data_Structures
AVL tree and Fibonacci Heap implementations

## Componants
- **AVLTreeList.py**: The main Python script for AVL tree operations including insertions, deletions, and balancing.
- **Tester_for_AVL_tree.py**: A Python testing script for verifying the correctness and efficiency of the AVL tree operations.
- **FibonacciHeap.java**: The main Java class that implements the Fibonacci heap data structure, supporting operations like insert, delete min, and meld.
- **Tester_for_fibonacci_heap.java**: A Java testing script for ensuring the Fibonacci heap operations work as expected under various scenarios.


## AVL Tree Implementation

### Overview
This project involves the implementation of an AVL tree using Python 3.9. It includes functions to manage tree operations while maintaining balance, as per the AVL tree properties.

### Features
- **Insert**: Add a value in the tree and balance the tree accordingly.
- **Delete**: Remove a value from the tree and rebalance.
- **Search**: Find the index of a value in the tree.
- **Traversal**: Supports various tree traversal methods to explore values.
- **Balance Maintenance**: Automatic balancing of the tree after insertions and deletions to ensure optimal performance.

### Functions
- `insert(i, s)`: Inserts a value `s` at position `i`.
- `delete(i)`: Deletes the value at position `i`.
- `search(val)`: Returns the first index with the value `val`.
- Other utility functions to support tree operations.

## Fibonacci Heap

### Overview
This project focuses on the implementation of a Fibonacci heap which is a collection of trees with minimum-heap or maximum-heap properties, used especially in priority queue operations.

### Features
- **Fast Insertion**: O(1) amortized time for insert operations.
- **Efficient Decrease Key and Delete Min**: Operations crucial for advanced algorithms like Dijkstra's and Prim's.
- **Merge Heaps**: Ability to merge two heaps in constant time.

### Functions
- `insert(int i)`: Inserts a new element with value `i`.
- `deleteMin()`: Removes and returns the smallest element.
- `findMin()`: Returns the minimum element without removing it.
- `meld(FibonacciHeap heap2)`: Merges another heap with this heap.

### Complexity
The project includes an analysis of time complexities for each operation, ensuring that each is optimized for the best possible performance in various scenarios.

---

Both projects are implemented with a focus on algorithm efficiency and proper data structure utilization. They include detailed documentation for each method and a comprehensive suite of automated tests to validate all functionalities.
