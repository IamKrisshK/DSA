a=int(input(":"))
def isPalindrome(x: int) -> bool:
    x=str(x)
    if len(x)<2:
        return True
    l=0
    r=len(x)-1
    while l<r:
        if x[l]!=x[r]:
            return False
        l+=1
        r-=1
    return True
print(isPalindrome(a))
