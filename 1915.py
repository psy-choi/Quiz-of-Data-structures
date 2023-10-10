import sys

input = sys.stdin.readline

m, n = map(int, input().split())

arr = [list(map(int, input().rstrip())) for _ in range(m)]
answer = 0

for i in range(m):
    for j in range(n):
        if i == 0 or j == 0 or not arr[i][j]:
            pass
        else:
            arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1
        answer = max(answer, arr[i][j])

print(answer * answer)
