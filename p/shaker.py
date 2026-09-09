class shaker_sort():
    def __new__(cls,arr:list)->list:
        left=0
        right = len(arr)-1
        while left<right:
        #left to right
            for i in range(left,right):
                if arr[i]>arr[i+1]:
                    arr[i],arr[i+1]=arr[i+1],arr[i]
            right-=1
        #right to left
            for j in range(right,left,-1):
                if arr[j]<arr[j-1]:
                    arr[j],arr[j-1]=arr[j-1],arr[j]
            left+=1
        return arr
