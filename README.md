# Experiment 1: Implementation and Performance Analysis of Interpolation Search

## Aim
To implement Interpolation Search algorithm and analyze its performance.

## Description
Interpolation Search is an improved searching technique for sorted arrays. It estimates the position of the target element using a mathematical formula instead of checking the middle element like Binary Search.

It works efficiently when the elements are uniformly distributed.

## Algorithm Steps

1. Start with low and high indexes.
2. Calculate the probable position using interpolation formula.
3. Compare the target element with the estimated position.
4. If the element is found, return the index.
5. If the target is larger, search the right portion.
6. Otherwise search the left portion.
7. Repeat until the element is found or the search space becomes empty.

## Complexity Analysis

| Case | Complexity |
|------|------------|
| Best Case | O(1) |
| Average Case | O(log log n) |
| Worst Case | O(n) |

## Space Complexity

O(1)

## Files

- interpolation_search.py

## Output

The program displays:
- Element position
- Number of comparisons
- Execution time
- Performance comparison with Binary Search

## Conclusion

Interpolation Search provides better performance than Binary Search for uniformly distributed sorted data.




# Experiment 2: Comparative Analysis of String Matching Algorithms

## Aim

To implement and compare Naive Search, Rabin-Karp, and KMP string matching algorithms.

## Description

String matching algorithms are used to find occurrences of a pattern inside a given text.

Algorithms implemented:

1. Naive String Matching
2. Rabin-Karp Algorithm
3. Knuth-Morris-Pratt (KMP) Algorithm


## Algorithm Details

### Naive Algorithm
Checks the pattern at every possible position in the text.

### Rabin-Karp
Uses hashing technique to compare pattern and text efficiently.

### KMP
Uses the LPS (Longest Prefix Suffix) array to avoid unnecessary comparisons.


## Complexity Analysis

| Algorithm | Best | Average | Worst |
|-----------|------|---------|-------|
| Naive | O(n) | O(nm) | O(nm) |
| Rabin-Karp | O(n+m) | O(n+m) | O(nm) |
| KMP | O(n+m) | O(n+m) | O(n+m) |


## Files

- string_matching.py


## Conclusion

KMP provides better performance for large texts because it avoids repeated comparisons.


# Experiment 3: Implementation of Kruskal's and Prim's Algorithm

## Aim

To implement Minimum Spanning Tree algorithms using Kruskal's and Prim's algorithms.

## Description

A Minimum Spanning Tree connects all vertices of a weighted graph with minimum total edge weight.

Algorithms:

- Kruskal's Algorithm
- Prim's Algorithm


## Kruskal Algorithm

Kruskal selects edges in increasing order of weight and uses Union-Find to avoid cycles.


## Prim Algorithm

Prim starts from a vertex and repeatedly selects the minimum weight edge connecting the tree.


## Complexity Analysis

| Algorithm | Complexity |
|-----------|------------|
| Kruskal | O(E log E) |
| Prim | O(E log V) |


## Space Complexity

O(V)


## Files

- mst.py


## Conclusion

Both algorithms generate the same Minimum Spanning Tree with minimum cost.

# Experiment 4: Single Source Shortest Path using Dijkstra Algorithm

## Aim

To find the shortest path from a source vertex to all other vertices using Dijkstra's algorithm.


## Description

Dijkstra's algorithm finds the shortest distance between vertices in a graph with non-negative edge weights.


## Algorithm Steps

1. Initialize distance of source as 0.
2. Select the vertex with minimum distance.
3. Update distances of adjacent vertices.
4. Repeat until all vertices are processed.


## Complexity Analysis

Time Complexity:

O((V + E) log V)


Space Complexity:

O(V)


## Files

- dijkstra.py


## Conclusion

Dijkstra's algorithm efficiently finds shortest paths in weighted graphs.

# Experiment 5: Finding Min-Max using Divide and Conquer

## Aim

To find minimum and maximum values of an array using Divide and Conquer technique.


## Description

The array is divided into smaller parts. Minimum and maximum values are found separately and combined.


## Algorithm Steps

1. Divide the array into two halves.
2. Find min and max of each half recursively.
3. Compare results from both halves.


## Complexity Analysis

Time Complexity:

O(n)


Space Complexity:

O(log n)


## Files

- min_max.py


## Conclusion

Divide and Conquer reduces the number of comparisons compared to the normal approach.

# Experiment 6: Matrix Chain Multiplication using Dynamic Programming

## Aim

To find the optimal order of matrix multiplication using Dynamic Programming.


## Description

Matrix Chain Multiplication determines the order of multiplication that minimizes the number of scalar multiplications.


## Algorithm

1. Create cost table.
2. Calculate minimum multiplication cost.
3. Store optimal split positions.
4. Print optimal parenthesization.


## Complexity Analysis

Time Complexity:

O(n³)


Space Complexity:

O(n²)


## Files

- matrix_chain.py


## Conclusion

Dynamic Programming provides an efficient solution by storing previous calculations.

# Experiment 7: N-Queens Problem using Backtracking

## Aim

To solve the N-Queens problem using Backtracking technique.


## Description

The N-Queens problem places N queens on an N×N chessboard such that no two queens attack each other.


## Algorithm Steps

1. Place queen row by row.
2. Check whether the position is safe.
3. If safe, continue recursively.
4. Otherwise backtrack and try another position.


## Complexity Analysis

Time Complexity:

O(N!)


Space Complexity:

O(N)


## Files

- n_queens.py


## Conclusion

Backtracking efficiently removes invalid possibilities and finds valid solutions.

# Experiment 8: Travelling Salesman Problem

## Aim

To find the minimum cost tour for Travelling Salesman Problem.


## Description

The Travelling Salesman Problem finds the shortest possible route that visits all cities exactly once and returns to the starting city.


## Algorithm

1. Generate possible routes.
2. Calculate cost of each route.
3. Select the minimum cost route.


## Complexity Analysis

Time Complexity:

O(n!)


Space Complexity:

O(n)


## Files

- tsp.py


## Conclusion

The algorithm finds the optimal tour but requires high computation for large inputs.

# Experiment 9: Efficient Bin Packing using Approximation Algorithm

## Aim

To implement approximation algorithms for Bin Packing problem.


## Algorithms Implemented

1. First Fit
2. First Fit Decreasing
3. Best Fit Decreasing


## Description

Bin Packing divides objects into minimum number of bins with fixed capacity.


## Complexity Analysis

| Algorithm | Complexity |
|-|-|
| First Fit | O(n²) |
| First Fit Decreasing | O(n log n + n²) |
| Best Fit Decreasing | O(n log n + n²) |


## Files

- bin_packing.py


## Conclusion

FFD and BFD provide better solutions compared to simple First Fit.


# Experiment 10: Improving Quick Sort Efficiency using Randomized Algorithm

## Aim

To compare Deterministic Quick Sort and Randomized Quick Sort performance.


## Description

Randomized Quick Sort selects a random pivot element to avoid worst-case scenarios.


## Algorithms

1. Deterministic Quick Sort
2. Randomized Quick Sort


## Complexity Analysis

| Algorithm | Best | Average | Worst |
|-|-|-|-|
| Deterministic Quick Sort | O(n log n) | O(n log n) | O(n²) |
| Randomized Quick Sort | O(n log n) | O(n log n) | O(n²) |


## Space Complexity

O(log n)


## Files

- randomized_quicksort.py


## Conclusion

Randomized Quick Sort provides better performance for sorted and nearly sorted inputs by avoiding poor pivot selection.
