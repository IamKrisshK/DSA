# Comparison Sorting Algorithms

| Name | Best | Average | Worst | Memory | Stable | In-place | Method | Other Notes |
|---|---:|---:|---:|---:|:---:|:---:|---|---|
| [**Heapsort**](./sortalgo.md#heapsort) | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(1)` | No | Yes | Selection | Optimized selection sort using a max heap to find the maximum in `O(log n)`. |
| [**Introsort**](./sortalgo.md#introsort) | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(log n)` | No | Yes | Partitioning & Selection | Combines Quicksort, Heapsort, and Insertion sort. Used in several STL implementations. |
| [**Merge sort**](./sortalgo.md#merge-sort) | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(n)` | Yes | No | Merging | Highly parallelizable. |
| [**In-Place Merge Sort**](./sortalgo.md#in-place-merge-sort) | `O(n)` | `O(n log² n)` | `O(n log² n)` | `O(log n)` | Yes | Yes | Merging | In-place stable merge variant. |
| [**Tournament sort**](./sortalgo.md#tournament-sort) | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(n)` | Yes | No | Selection | Uses a tournament tree. |
| [**Tree sort**](./sortalgo.md#tree-sort) | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(n)` | Yes | No | Insertion | Uses a self-balancing BST. |
| [**Block sort**](./sortalgo.md#block-sort) | `O(n)` | `O(n log n)` | `O(n log n)` | `O(1)` | Yes | Yes | Insertion & Merging | Block-based in-place merge sort. |
| [**Smoothsort**](./sortalgo.md#smoothsort) | `O(n)` | `O(n log n)` | `O(n log n)` | `O(1)` | No | Yes | Selection | Adaptive Heapsort using Leonardo numbers. |
| [**Timsort**](./sortalgo.md#timsort) | `O(n)` | `O(n log n)` | `O(n log n)` | `O(n)` | Yes | No | Insertion & Merging | Uses naturally occurring sorted runs. |
| [**Patience sorting**](./sortalgo.md#patience-sorting) | `O(n)` | `O(n log n)` | `O(n log n)` | `O(n)` | No | No | Insertion & Selection | Based on card-game patience sorting. |
| [**Cubesort**](./sortalgo.md#cubesort) | `O(n)` | `O(n log n)` | `O(n log n)` | `O(n)` | Yes | No | Insertion | Stable adaptive sorting algorithm. |
| [**Quicksort**](./sortalgo.md#quicksort) | `O(n log n)` | `O(n log n)` | `O(n²)` | `O(log n)` | No | Yes | Partitioning | Pivot-based partitioning. |
| [**Fluxsort**](./sortalgo.md#fluxsort) | `O(n)` | `O(n log n)` | `O(n log n)` | `O(n)` | Yes | No | Partitioning & Merging | Adaptive branchless stable introsort. |
| [**Crumsort**](./sortalgo.md#crumsort) | `O(n)` | `O(n log n)` | `O(n log n)` | `O(log n)` | No | Yes | Partitioning & Merging | In-place unstable Fluxsort variant. |
| [**Library sort**](./sortalgo.md#library-sort) | `O(n log n)` | `O(n log n)` | `O(n²)` | `O(n)` | No | No | Insertion | Gapped insertion sort. |
| [**Shellsort**](./sortalgo.md#shellsort) | `O(n log n)` | `Ω(n log n)` | `O(n^(1+1/k))` | `O(1)` | No | Yes | Insertion | Gap-based insertion sort. |
| [**Comb sort**](./sortalgo.md#comb-sort) | `O(n log n)` | `O(n²)` | `O(n²)` | `O(1)` | No | Yes | Exchanging | Improved Bubble sort. |
| [**Insertion sort**](./sortalgo.md#insertion-sort) | `O(n)` | `O(n²)` | `O(n²)` | `O(1)` | Yes | Yes | Insertion | Inserts each element into its correct position. |
| [**Bubble sort**](./sortalgo.md#bubble-sort) | `O(n)` | `O(n²)` | `O(n²)` | `O(1)` | Yes | Yes | Exchanging | Repeatedly swaps adjacent elements. |
| [**Cocktail shaker sort**](./sortalgo.md#cocktail-shaker-sort) | `O(n)` | `O(n²)` | `O(n²)` | `O(1)` | Yes | Yes | Exchanging | Bidirectional Bubble sort. |
| [**Gnome sort**](./sortalgo.md#gnome-sort) | `O(n)` | `O(n²)` | `O(n²)` | `O(1)` | Yes | Yes | Exchanging | Moves backward after swaps. |
| [**Odd–even sort**](./sortalgo.md#odd-even-sort) | `O(n)` | `O(n²)` | `O(n²)` | `O(1)` | Yes | Yes | Exchanging | Easily parallelizable. |
| [**Strand sort**](./sortalgo.md#strand-sort) | `O(n)` | `O(n²)` | `O(n²)` | `O(n)` | Yes | No | Selection | Extracts and merges sorted strands. |
| [**Selection sort**](./sortalgo.md#selection-sort) | `O(n²)` | `O(n²)` | `O(n²)` | `O(1)` | No | Yes | Selection | Repeatedly selects the minimum. |
| [**Cycle sort**](./sortalgo.md#cycle-sort) | `O(n²)` | `O(n²)` | `O(n²)` | `O(1)` | No | Yes | Selection | Minimizes the number of writes. |

---

# Non-Comparison Sorting Algorithms

| Name | Best | Average | Worst | Memory | Stable | `n ≪ 2^k` | Notes |
|---|---:|---:|---:|---:|:---:|:---:|---|
| [**Pigeonhole sort**](./sortalgo.md#pigeonhole-sort) | — | `O(n + 2^k)` | `O(n + 2^k)` | `O(2^k)` | Yes | Yes | Integer values only. |
| [**Bucket sort (uniform keys)**](./sortalgo.md#bucket-sort-uniform-keys) | — | `O(n + k)` | `O(n² · k)` | `O(n · k)` | Yes | No | Assumes uniform distribution. |
| [**Bucket sort (integer keys)**](./sortalgo.md#bucket-sort-integer-keys) | — | `O(n + r)` | `O(n + r)` | `O(n + r)` | Yes | Yes | Efficient when `r = O(n)`. |
| [**Counting sort**](./sortalgo.md#counting-sort) | — | `O(n + r)` | `O(n + r)` | `O(n + r)` | Yes | Yes | Counts occurrences of each value. |
| [**LSD Radix Sort**](./sortalgo.md#lsd-radix-sort) | `O(nk/d)` | `O(nk/d)` | `O(nk/d)` | `O(n + 2^d)` | Yes | No | Processes digits from least significant to most significant. |
| [**MSD Radix Sort**](./sortalgo.md#msd-radix-sort) | `O(n)` | `O(nk/d)` | `O(nk/d)` | `O(n + 2^d)` | Yes | No | Processes digits from most significant to least significant. |
| [**MSD Radix Sort (in-place)**](./sortalgo.md#msd-radix-sort-in-place) | `O(n)` | `O(nk)` | `O(nk)` | `O(1)` | No | No | In-place MSD radix sort. |
| [**Spreadsort**](./sortalgo.md#spreadsort) | `O(n)` | `O(nk/d)` | `O(n(k/s+d))` | `O((k/d)2^d)` | No | No | Hybrid distribution/comparison sort. |
| [**Burstsort**](./sortalgo.md#burstsort) | — | `O(nk/d)` | `O(nk/d)` | `O(nk/d)` | No | No | Optimized for strings. |
| [**Flashsort**](./sortalgo.md#flashsort) | `O(n)` | `O(n+r)` | `O(n²)` | `O(n)` | No | No | Distribution-based sort. |

---

# Other Sorting Algorithms

| Name | Best | Average | Worst | Memory | Stable | Comparison | Other Notes |
|---|---:|---:|---:|---:|:---:|:---:|---|
| [**Bead sort**](./sortalgo.md#bead-sort) | `O(n)` | `O(S)` | `O(S)` | `O(n²)` | N/A | No | Positive integers only. |
| [**Merge-insertion sort**](./sortalgo.md#merge-insertion-sort) | `O(n log n)` | `O(n log n)` | `O(n log n)` | Varies | No | Yes | Minimizes comparisons. |
| [**Spaghetti (Poll) sort**](./sortalgo.md#spaghetti-poll-sort) | `O(n)` | `O(n)` | `O(n)` | `O(n²)` | Yes | Polling | Uses parallel processors. |
| [**Sorting network**](./sortalgo.md#sorting-network) | Varies | Varies | Varies | Varies | Varies | Yes | Fixed comparison sequence. |
| [**Bitonic sorter**](./sortalgo.md#bitonic-sorter) | `O(log² n)` | `O(log² n)` | `O(n log² n)` | `O(1)` | No | Yes | Sorting-network variant. |
| [**Bogosort**](./sortalgo.md#bogosort) | `O(n)` | `O(n · n!)` | Unbounded | `O(1)` | No | Yes | Randomly shuffles until sorted. |
| [**Stooge sort**](./sortalgo.md#stooge-sort) | `O(n^2.7095)` | `O(n^2.7095)` | `O(n^2.7095)` | `O(log n)` | No | Yes | Recursively sorts overlapping `2/3` sections. |
| [**Slowsort**](./sortalgo.md#slowsort) | `o(n^(log₂(n)/2))` | `o(n^(log₂(n)/2))` | `o(n^(log₂(n)/2))` | `O(n)` | No | Yes | Deliberately inefficient sorting algorithm. |

---

# Sorting Performance — 2048 Random Items

| Algorithm | Time (seconds) |
|---|---:|
| [**Bubble sort**](./sortalgo.md#bubble-sort) | `128.84` |
| [**Shaker sort**](./sortalgo.md#cocktail-shaker-sort) | `104.44` |
| [**Selection sort**](./sortalgo.md#selection-sort) | `58.34` |
| [**Insertion sort**](./sortalgo.md#insertion-sort) | `50.74` |
| **Binary insertion sort** | `37.66` |
| [**Shell sort**](./sortalgo.md#shellsort) | `7.08` |
| [**Heap sort**](./sortalgo.md#heapsort) | `2.22` |
| [**Merge sort**](./sortalgo.md#merge-sort) | `2.06` |
| **Non-recursive quicksort** | `1.32` |
| [**Quicksort**](./sortalgo.md#quicksort) | `1.22` |
