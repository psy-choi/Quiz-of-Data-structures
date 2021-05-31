# Quiz-of-Data-structures
# BJ10818 solution
import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
Mx = lst[0]
Mi = lst[0]
for i in range(1, N):
    if lst[i] > Mx:
        Mx = lst[i]
    if lst[i] < Mi:
        Mi = lst[i]
print(Mi,Mx)
# 이렇게 하나하나 비교해서 최댓값 최솟값을 도출해야 함
# 함수로는 min, max함수를 사용해서 활용 가능
