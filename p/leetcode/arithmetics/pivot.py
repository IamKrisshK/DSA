def pivotInteger(n: int) -> int:
    lsum=1
    rsum=n
    l=1
    r=n
    while l<r:
        if lsum<rsum:
            l+=1
            lsum+=l
        else:
            r-=1
            rsum+=r
    return l if lsum==rsum else -1
print(pivotInteger(8))
