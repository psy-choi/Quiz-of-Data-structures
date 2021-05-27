#처음 풀었던 답. 시간 초과가 나와 다른 방법을 구현해야 했음
import sys
N = 0
M = 0
def fibonacci(n):
    global N
    global M
    if n == 0:
        N += 1
        return 0
    elif n == 1:
        M += 1
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

K = int(sys.stdin.readline())
for i in range(K):
    fibonacci(i)
    print(N, M)
    N = 0
    M = 0
#시간 초과가 나오지 않기 위해서 피보나치 수열을 직접 돌리기 보다는, 0과 1이 나오는 숫자만 구하는 구현식이 필요!
import sys

Zero = [1,0,1]
One = [0,1,1]

def fibonaccicall(n):
    global Zero
    global One
    if n >= len(Zero):
        for i in range(len(Zero), n+1):
            Zero.append(Zero[i-1]+Zero[i-2])
            One.append(One[i-1]+One[i-2])
        return print(Zero[n],One[n])
    else:
        return print(Zero[n],One[n])

K = int(sys.stdin.readline())
for i in range(K):
    fibonaccicall(int(sys.stdin.readline()))
