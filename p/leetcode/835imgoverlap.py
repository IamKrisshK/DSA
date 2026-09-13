def largestOverlap(img1: List[List[int]], img2: List[List[int]]) -> int:
    n = len(img1)
    ans = 0
    for x in range(-n + 1, n):
        for y in range(-n + 1, n):
            k = []
            for i in range(n):
                row = []
                for j in range(n):
                    ni = i + x
                    nj = j + y
                    if 0 <= ni < n and 0 <= nj < n:
                        row.append(img1[i][j] - img2[ni][nj])
                    else:
                        row.append(-1)
                k.append(row)
            overlap = 0
            for i in range(n):
                for j in range(n):
                    if k[i][j] == 0 and img1[i][j] == 1:
                        overlap += 1
            ans = max(ans, overlap)
    return ans
img1 = [[1,1,0],[0,1,0],[0,1,0]]; img2 = [[0,0,0],[0,1,1],[0,0,1]]
print(largestOverlap(img1,img2))
