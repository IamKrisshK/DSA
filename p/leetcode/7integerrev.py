x=123
x=str(x)
if len(x)<2:
    print(int(x))
res=""
if x[0]=="-":
    #neg number
    x=x[1:]
    res+="-"
length = len(x)-1
while x[length]=='0':
    length-=1
for i in range(length,-1,-1):
    res+=x[i]
res=int(res)
print(res if (res<(2**31)-1 and res>(-2)**31) else 0)
