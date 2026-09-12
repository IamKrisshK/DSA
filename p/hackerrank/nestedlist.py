from math import inf


if __name__ == '__main__':
    a={}
    lowest=inf
    second_low=inf
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a[name]=score
    scores = sorted(set(a.values()))
    second_low = scores[1]
    for name in reversed(a):
        print(a)
        if a[name] == second_low:
            print(name)
