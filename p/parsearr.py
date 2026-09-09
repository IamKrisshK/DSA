class parser():
    def __new__(cls) -> list:
        arr=input("Enter list: ")
        arr=arr.split()
        arr=[int(i) for i in arr]
        return arr
