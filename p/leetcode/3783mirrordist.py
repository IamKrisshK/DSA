def mirrorDistance(n: int) -> int:
    return abs(n-int(str(n)[::-1]))
