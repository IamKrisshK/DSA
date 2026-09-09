s="1234567890"
def convert(s:str,numrows:int):
    if numrows==1 or numrows>len(s):
        return s
    res=[""]*numrows
    row=0
    dir=1
    for ch in s:
        res[row]+=ch
        if row==0:
            dir=1
        elif row==numrows-1:
            dir=-1
        row+=dir
    a= "".join(res)
    print(a)
convert(s,4)
