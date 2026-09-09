# Sorting Algorithms

## Table of Contents

- [Comparison Sorts](#comparison-sorts)
- [Non-Comparison Sorts](#non-comparison-sorts)
- [Other Sorting Algorithms](#other-sorting-algorithms)

---

## Comparison Sorts

### 1. Heapsort
1. Build a max heap.
2. Swap root with the last element.
3. Reduce heap size.
4. Heapify the root.
5. Repeat until sorted.

### 2. Introsort
1. Start with Quicksort.
2. Track recursion depth.
3. Switch to Heapsort if the depth limit is exceeded.
4. Use Insertion sort for small partitions.

### 3. Merge Sort
1. Divide the array into two halves.
2. Recursively sort both halves.
3. Merge the sorted halves.
4. Repeat until sorted.

### 4. In-Place Merge Sort
1. Divide the array into two halves.
2. Recursively sort both halves.
3. Merge the halves in-place.
4. Repeat until sorted.

### 5. Tournament Sort
1. Build a tournament tree.
2. Select the minimum/maximum at the root.
3. Remove the selected element.
4. Update the tree.
5. Repeat.

### 6. Tree Sort
1. Insert all elements into a BST.
2. Balance the tree if required.
3. Perform inorder traversal.
4. Output the traversal.

### 7. Block Sort
1. Divide the array into blocks.
2. Sort individual blocks.
3. Merge blocks in-place.
4. Repeat until one sorted sequence remains.

### 8. Smoothsort
1. Build Leonardo heaps.
2. Maintain heap ordering.
3. Extract the maximum.
4. Restore the Leonardo heap.
5. Repeat.

### 9. Timsort
1. Detect naturally sorted runs.
2. Extend short runs using Insertion sort.
3. Store runs on a stack.
4. Merge runs according to size rules.
5. Continue until one run remains.

### 10. Patience Sorting
1. Place each element on the leftmost valid pile.
2. Maintain pile tops in sorted order.
3. Extract elements from the piles.
4. Produce the sorted sequence.

### 11. Cubesort
1. Insert elements into ordered cube structures.
2. Maintain ordering during insertion.
3. Partition structures when necessary.
4. Traverse structures in sorted order.

### 12. Quicksort
1. Select a pivot.
2. Partition elements around the pivot.
3. Recursively sort both partitions.
4. Stop when partitions contain ≤1 element.

### 13. Fluxsort
1. Detect ordered regions.
2. Partition around pivots.
3. Recursively process partitions.
4. Merge partitions stably when required.

### 14. Crumsort
1. Partition the array around pivots.
2. Perform in-place partitioning.
3. Recursively sort partitions.
4. Merge where required.

### 15. Library Sort
1. Insert elements into a sparse array.
2. Maintain gaps between elements.
3. Find insertion positions using binary search.
4. Shift elements into available gaps.
5. Rebalance when gaps are exhausted.

### 16. Shellsort
1. Choose a gap sequence.
2. Perform insertion sort using the current gap.
3. Reduce the gap.
4. Repeat until gap = 1.

### 17. Comb Sort
1. Choose a large gap.
2. Compare elements separated by the gap.
3. Swap unordered elements.
4. Shrink the gap.
5. Repeat until sorted.

### 18. Insertion Sort
1. Select the next element.
2. Compare it with preceding elements.
3. Shift larger elements right.
4. Insert the element at its correct position.
5. Repeat.

### 19. Bubble Sort
1. Compare adjacent elements.
2. Swap if they are out of order.
3. Repeat passes through the array.
4. Stop when no swaps occur.

### 20. Cocktail Shaker Sort
1. Traverse left-to-right and swap adjacent elements.
2. Traverse right-to-left and swap adjacent elements.
3. Shrink both boundaries.
4. Repeat until sorted.

### 21. Gnome Sort
1. Compare adjacent elements.
2. Move forward if they are ordered.
3. Swap and move backward if unordered.
4. Repeat until the end.

### 22. Odd-Even Sort
1. Compare odd-even pairs.
2. Swap unordered pairs.
3. Compare even-odd pairs.
4. Repeat until no swaps occur.

### 23. Strand Sort
1. Extract an increasing subsequence.
2. Remove it from the input.
3. Merge it into the output.
4. Repeat until the input is empty.

### 24. Selection Sort
1. Find the minimum element.
2. Swap it with the first unsorted element.
3. Move the boundary forward.
4. Repeat.

### 25. Cycle Sort
1. Determine the correct position of an element.
2. Place it in that position.
3. Displace the existing element.
4. Continue the cycle.
5. Repeat for remaining elements.

---

## Non-Comparison Sorts

### 26. Pigeonhole Sort
1. Find the minimum and maximum.
2. Create holes for possible values.
3. Place elements into their corresponding holes.
4. Traverse the holes in order.

### 27. Bucket Sort — Uniform Keys
1. Create buckets.
2. Map each element to a bucket.
3. Sort each bucket.
4. Concatenate the buckets.

### 28. Bucket Sort — Integer Keys
1. Determine the integer range.
2. Create buckets for the range.
3. Place each integer into its bucket.
4. Output the buckets sequentially.

### 29. Counting Sort
1. Find the value range.
2. Create a count array.
3. Count each element.
4. Compute cumulative counts.
5. Place elements using the counts.

### 30. LSD Radix Sort
1. Start with the least significant digit.
2. Stable-sort elements by that digit.
3. Move to the next digit.
4. Repeat through the most significant digit.

### 31. MSD Radix Sort
1. Start with the most significant digit.
2. Partition elements by that digit.
3. Recursively sort each partition using the next digit.
4. Stop when partitions contain ≤1 element.

### 32. MSD Radix Sort — In-Place
1. Select the most significant digit.
2. Partition elements in-place by digit.
3. Recursively process each partition.
4. Continue through remaining digits.

### 33. Spreadsort
1. Estimate the value range.
2. Spread elements into bins.
3. Recursively subdivide dense bins.
4. Sort small bins using a comparison sort.
5. Concatenate the bins.

### 34. Burstsort
1. Store strings in a trie-like structure.
2. Insert strings into buckets.
3. Split overloaded buckets.
4. Traverse buckets lexicographically.

### 35. Flashsort
1. Estimate the value distribution.
2. Classify elements into classes.
3. Permute elements into their classes.
4. Sort each class.
5. Combine the classes.

---

## Other Sorting Algorithms

### 36. Bead Sort
1. Represent each number using beads.
2. Drop beads under gravity.
3. Count bead positions.
4. Convert positions back into numbers.

### 37. Merge-Insertion Sort
1. Pair the elements.
2. Compare elements within each pair.
3. Recursively sort the larger elements.
4. Insert smaller elements using binary insertion.
5. Produce the sorted sequence.

### 38. Spaghetti (Poll) Sort
1. Represent each element with a stick proportional to its value.
2. Stand all sticks vertically.
3. Identify the tallest stick.
4. Remove it.
5. Repeat and output in order.

### 39. Sorting Network
1. Arrange elements into fixed comparator stages.
2. Compare predetermined pairs.
3. Swap unordered pairs.
4. Execute all stages.
5. Output the sorted elements.

### 40. Bitonic Sorter
1. Build bitonic sequences.
2. Compare and exchange elements at fixed distances.
3. Recursively merge bitonic sequences.
4. Repeat until sorted.

### 41. Bogosort
1. Check whether the array is sorted.
2. Randomly shuffle if it is not.
3. Repeat until sorted.

### 42. Stooge Sort
1. Compare the first and last elements.
2. Swap if necessary.
3. Recursively sort the first `2/3`.
4. Recursively sort the last `2/3`.
5. Recursively sort the first `2/3` again.

### 43. Slowsort
1. Recursively sort the first portion.
2. Recursively sort the remaining portion.
3. Compare the maximum with the last element.
4. Swap if necessary.
5. Recursively repeat on a smaller portion.
