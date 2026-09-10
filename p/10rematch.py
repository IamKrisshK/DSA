s = "aaaaaaa"
p = "a*a"

def isMatch(s, p):
    m = {}
    def f(i, j):
        if (i,j) in m: return m[i,j]
        if j == len(p): return i == len(s)
        x = i < len(s) and (p[j] == '.' or s[i] == p[j])
        if j+1 < len(p) and p[j+1] == '*':
            r = f(i,j+2) or (x and f(i+1,j))
        else: r = x and f(i+1,j+1)
        m[i,j] = r
        return r
    return f(0,0)

print(isMatch(s,p))
