def minSumOfLengths(arr: list[int], target: int) -> int:
    INF = len(arr) + 1
    ans = INF
    left = 0
    total = 0
    best_at = [INF] * len(arr)
    for right, x in enumerate(arr):
        total += x
        while total > target:
            total -= arr[left]
            left += 1
        if right:
            best_at[right] = best_at[right - 1]
        if total == target:
            length = right - left + 1
            if left > 0 and best_at[left - 1] != INF:
                ans = min(ans, length + best_at[left - 1])
            best_at[right] = min(best_at[right], length)
    return -1 if ans == INF else ans
