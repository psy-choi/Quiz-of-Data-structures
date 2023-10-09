import sys

input = sys.stdin.readline

N, S = map(int, input().split())
Num_list = list(map(int, input().split()))
Num_list.sort()

length = len(Num_list)

cnt = 0

# i 의 값을 더하고, num은 i를 더하기 이전의 값
def tracking(num, i):
    global cnt
    if num + Num_list[i] == S:
        cnt += 1
    if i+1 == length:
        return
    if (num > S and Num_list[i+1] > 0):
        return
    tracking(num + Num_list[i], i+1)
    tracking(num, i + 1)

tracking(0, 0)
print(cnt)
