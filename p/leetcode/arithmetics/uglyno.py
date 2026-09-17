def isUgly(n: int) -> bool:
        if n<1:
            return False
        while True:
            n=n/2 if n%2==0 and n>=2 else n
            n=n/3 if n%3==0 and n>=3 else n
            n=n/5 if n%5==0 and n>=5 else n
            if n==1:
                return True
                break
            if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
                return False
