if __name__ == '__main__':
    k, m = map(int, input().split())
    values = {0}
    for _ in range(k):
        arr = list(map(int, input().split()))[1:]
        values = {(x + a * a) % m for x in values for a in arr}
    print(max(values))
