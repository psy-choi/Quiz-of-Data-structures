import sys
dic = {(20,20,20):1048576}

def w(a,b,c):
    K = (a,b,c)
    if K in dic:
        return dic[K]
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if a < b < c:
        if (a,b,c) not in dic:
            dic[(a,b,c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        if (a, b, c) not in dic:
            dic[(a,b,c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

while True:
    A,B,C = map(int, sys.stdin.readline().split())
    if A == -1 and B == -1 and C == -1:
        break
    k = w(A,B,C)
    print("w({0}, {1}, {2}) = {3}".format(A,B,C,k))
