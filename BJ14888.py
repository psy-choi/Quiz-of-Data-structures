#내가 쓴 답변 -> 이걸로 하면 시간 초과가 나왔다.

import sys
from itertools import permutations
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
plus, minus, multiple, division = map(int, sys.stdin.readline())
operation = []
operation += ["+"]*plus
operation += ["-"]*minus
operation += ["*"]*multiple
operation += ["/"]*division
operation_permutation = []
for i in list(permutations(operation)):
    operation_permutation.append(i)

max = -1000000001
min = 1000000001
for case in operation_permutation:
    answer = a[0]
    for i in range(N-1):
        if case[i] == "+":
            answer += a[i+1]
        elif case[i] == "-":
            answer -= a[i+1]
        elif case[i] == "-":
            answer -= a[i+1]
        else:
            if answer < 0:
                answer = -(-(answer) // a[i+1])
            else:
                answer //= a[i+1]
    if answer > max:
        max = answer
    if min > answer:
        min = answer
print(max)
print(min)


#참조해서 쓴 재귀함수 답변
import sys
N = int(sys.stdin.readline())
Ma = -1000000001
Mi = 100000001
arr = list(map(int, sys.stdin.readline().split()))
def operation(num, idx, add, sub, mul, div):
    global Ma, Mi, arr
    if idx == N-1:
        Ma = max(Ma, num)
        Mi = min(Mi, num)
        return
    if 0 < add:
        operation(num+arr[idx+1], idx+1, add-1, sub, mul, div)
    if 0 < sub:
        operation(num-arr[idx+1], idx+1, add, sub-1, mul, div)
    if 0 < mul:
        operation(num*arr[idx + 1], idx + 1, add, sub, mul-1, div)
    if 0 < div:
        if num < 0:
            operation(-(-num//arr[idx + 1]), idx + 1, add, sub, mul, div-1)
        else:
            operation(num // arr[idx + 1], idx + 1, add, sub, mul, div - 1)



a, b, c, d = map(int, sys.stdin.readline().split())
operation(arr[0],0,a,b,c,d)
print(Ma)
print(Mi)
#재귀 함수를 통해서 연산자를 나타내는 방법! 재귀 함수를 어떻게 활용하면 좋을지 항상 생각해보자~
