def countCommas(n: int) -> int:
    return sum(max(0, n-10**i+1) for i in range(3, len(str(n)), 3))
