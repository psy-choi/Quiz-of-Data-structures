# 친구 관계만으로 이동할 수 있는 사이를 의미한다.
import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

n, m = map(int, input().split())

friend = [i for i in range(n+1)]

def get_parent(a):
    global friend
    if a != friend[a]:
        friend[a] = get_parent(friend[a])
    return friend[a]


def union(a, b):
    global friend
    
    p_b = get_parent(b)
    p_a = get_parent(a)
    if p_a < p_b:
        friend[p_b] = p_a
    elif p_a > p_b:
        friend[p_a] = p_b
    else:
        return

def same(a, b):
    global friend
    p_b = get_parent(b)
    p_a = get_parent(a)
    if p_a != p_b:
        return False
    else:
        return True

for _ in range(m):
    cal, a, b = map(int, input().split())
    if cal == 1:
        if same(a, b): print("YES")
        else : print("NO")
    else:
        union(a, b)
