# Quiz-of-Data-structures
import sys
A, B = map(int, sys.stdin.readline().split())
#유클리드 호제법
a, b = A, B
while b != 0:
    a %= b
    a,b = b,a

print(a)
print(A*B//a) #//로 표현하는 것은 float값으로 하지 않기 위함.
