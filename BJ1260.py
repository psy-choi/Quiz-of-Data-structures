import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())
vic = {}
for i in range(N):
    vic[i+1] = []
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    vic[a].append(b)
    vic[b].append(a)
def DFS(maj,v):
    stack = []
    check = []
    stack.append(v)
    while len(stack) != 0:
        k = stack.pop(-1)
        if k not in check:
            check.append(k)
        for j in sorted(maj[k], reverse=True):
            if j not in check:
                stack.append(j)
    for i in check:
        print(i, end=" ")

def BFS(maj,v):
    queue = deque()
    check = []
    queue.append(v)
    while len(queue) != 0:
        k = queue.popleft()
        if k not in check:
            check.append(k)
        for j in sorted(maj[k]):
            if j not in check:
                queue.append(j)
    for i in check:
        print(i, end=" ")

DFS(vic,V)
print()
BFS(vic,V)
