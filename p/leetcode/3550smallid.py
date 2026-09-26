def smallestIndex(nums: List[int]) -> int:
    for i in range(len(nums)):
        a = str(nums[i])
        a=a.replace("","+")
        a = eval(a[1:-1])
        if a==i:
            return i
    return -1
def smallestIndex2(nums: List[int]) -> int:
    for i in range(len(nums)):
        def sum_digits(n):
            r = 0
            while n:
                r, n = r + n % 10, n // 10
            return r
        if i==sum_digits(nums[i]):
            return i
    return  -1
nums=[1,3,2]
print(smallestIndex(nums))
