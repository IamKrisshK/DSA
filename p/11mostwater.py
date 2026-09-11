def maxArea(height: List[int]) -> int:
    l=0
    r=len(height)-1
    maximum=0
    while l<r:
        k=min(height[l],height[r])
        maximum=max(maximum,k*(r-l))
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return maximum
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
