def minOperations(nums: list[int], x: int) -> int:
    t=sum(nums)-x;l=s=a=0
    if t<0:return -1
    for r,v in enumerate(nums):
        s+=v
        while s>t:s-=nums[l];l+=1
        if s==t:a=max(a,r-l+1)
    return len(nums)-a if a or t==0 else -1
