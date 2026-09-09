s=input(":")
def myAtoi( s: str) -> int:
    res=""
    l=0
    sign=1
    if len(s)<1:
        return 0
    #for whitespace
    while l<len(s) and s[l] ==" ":
        l+=1
    s=s[l:]
    if len(s)<1:
        return 0
    #return early if alpha
    if s[0].isalpha():
        return 0
    #check for signs
    if s[0] in ('+','-'):
        sign=-1 if s[0]=="-" else 1
        s=s[1:]
    #strip 0s
    if len(s)<1:
        return 0
    l=0
    for i in range(len(s)):
        if s[l]=='0':
            l+=1
    s=s[l:]
    if len(s)<1:
        return 0
    #check decimal place
    if not s[0].isdecimal():
        return 0
    if s[0] == '.':
        res+='0.'
        s=s[1:]
    for i in range(0,len(s)):
        if s[i].isdecimal():
            res+=s[i]
        else:
            break
    a=0
    for ch in res:
        a = a * 10 + (ord(ch) - ord('0'))
    a*=sign
    if a < -2**31:
        return -2**31
    if a > 2**31 - 1:
        return 2**31 - 1
    return a
a=myAtoi(s)
print(a)
