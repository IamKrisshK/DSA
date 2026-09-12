def lister(x,y,z,n):
    A=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                A.append([i,j,k]) if i+j+k!=n and [i,j,k] not in A else None
    return A
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(lister(x,y,z,n))
