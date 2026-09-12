def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr.sort()
    diff=arr[0]-arr[1]
    i=1
    while i<len(arr)-1:
        if arr[i]-arr[i+1]!=diff:
            return False
        i+=1
    return True
arr = [3,5,1]
print(canMakeArithmeticProgression(arr))
