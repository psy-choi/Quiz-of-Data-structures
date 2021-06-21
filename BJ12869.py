# Quiz-of-Data-structures
# 백준 12869번 문제
# dp를 사용해서 풀어야 한다고 하지만, BFS를 사용해서 풀었음
# visited라는 list를 생성하여 중복되는 경우를 삭제해주는 것이 중요함.
import sys
from collections import deque
SCV = int(sys.stdin.readline())
if SCV == 1:
    SCV_HP = int(sys.stdin.readline())
    if SCV_HP % 9 == 0:
        print(int(SCV_HP / 9))
    else:
        print(int(SCV_HP//9)+1)
    exit(0)
elif SCV == 2:
    a, b = map(int, sys.stdin.readline().split())
    lst = deque()
    lst.append([0,0,0])
    visited = []
    dx = [3, 9]
    dy = [9, 3]
    while True:
        A, B, C = lst.popleft()
        for i in range(2):
            Ax = dx[i] + A
            By = dy[i] + B
            if Ax >= a and By >= b:
                print(C+1)
                exit(0)
            if [Ax, By, C+1] in visited:
                continue
            else:
                lst.append([Ax, By, C+1])
                visited.append([Ax, By, C+1])
elif SCV == 3:
    a, b, c = map(int, sys.stdin.readline().split())
    lst = deque()
    visited = []
    lst.append([0,0,0,0])
    dx = [1, 1, 3, 3, 9, 9]
    dy = [3, 9, 1, 9, 1, 3]
    dz = [9, 3, 9, 1, 3, 1]
    while True:
        A, B, C, D = lst.popleft()
        for k in range(6):
                Ax = A + dx[k]
                By = B + dy[k]
                Cz = C + dz[k]
                if Ax >= a and By >= b and Cz >= c:
                    print(D+1)
                    exit(0)
                if [Ax, By, Cz, D+1] not in visited:
                    lst.append([Ax, By, Cz, D+1])
                    visited.append([Ax, By, Cz, D+1])
                else:
                    continue
                    
    #다른 것들 찾아보니까 깔끔하게 함수를 활용하는 것도 괜찮은 것 같다.
