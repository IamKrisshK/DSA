def resultArray(nums: List[int], k: int) -> List[int]:
    a = [0]*k
    d = [0]*k
    for x in nums:
        n = [0]*k
        x %= k
        n[x] = 1
        for r in range(k):
            n[r*x%k] += d[r]
        for r in range(k):
            a[r] += n[r]
        d = n
    return a
