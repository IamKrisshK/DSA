def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    m = min(len(i) for i in strs)
    l = 0
    while l < m:
        ch = strs[0][l]
        for i in strs:
            if i[l] != ch:
                return strs[0][:l]
        l += 1
    return strs[0][:m]
a=["flower","flow","gflight"]
print(longestCommonPrefix(a))
