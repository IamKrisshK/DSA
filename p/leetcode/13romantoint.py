def romanToInt(s: str) -> int:
    a={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    res=0
    prev=0
    for i in range(len(s)-1,-1,-1):
        if a[s[i]]<prev:
            res-=(a[s[i]])
        else:
            res+=a[s[i]]
        prev=a[s[i]]
    return res
a='MCMXCIV'
print(romanToInt(a))
