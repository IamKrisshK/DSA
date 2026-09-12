import numpy
if __name__ == '__main__':
    A=[]
    for _ in range(2):
        A.append(list(map(int, input().split())))
    print(numpy.inner(A[0],A[1]))
    print(numpy.outer(A[0],A[1]))
