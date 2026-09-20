def reverseDegree(s: str) -> int:
        sum=0
        for i in range(len(s)):
            sum+=(i+1)*(26-(ord(s[i])-97))
        return sum
