import sys
N, K = map(int, sys.stdin.readline().split())
divisor = []
divisor_k = 0
while divisor_k != N:
    divisor_k += 1
    if N % divisor_k == 0:
        divisor.append(divisor_k)
if len(divisor) >= K:
    print(divisor[K-1])
else:
    print(0)
    
# 처음 짠 코드가 밑에 있는 코드인데 왜 시간 초과가 나오는 걸까?
# while break구문을 통해서 모든 숫자를 다 하지 넣지 않아도 될텐데.
#이론 상으로는 더 효율적이지 않을까?
import sys
N, K = map(int, sys.stdin.readline().split())
divisor = []
divisor_k = 0
cnt = 0
while True:
    divisor_k += 1
    if N % divisor_k == 0:
        divisor.append(divisor_k)
        cnt += 1
    if cnt == K:
        break
if len(divisor) >= K:
    print(divisor[K-1])
else:
    print(0)
