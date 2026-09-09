class bubble_sort():
    def __new__(cls,arr:list) -> list:
        for i in range(len(arr)-1):
            s=False
            for j in range(len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    s=True
            if not s:
                break
        return arr
