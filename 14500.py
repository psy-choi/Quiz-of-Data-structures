N, M = map(int, input().split()) # y, x

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
# 2개
# 1개
# 4개
# 2개
# 4개


cnt = 0
for k in range(N):
    for j in range(M):
        new_cnt = 0
        if (k +3) < N:
            cnt = max(cnt, (lst[k][j] + lst[k+1][j] + lst[k+2][j] + lst[k+3][j]))
        if (j + 3) < M:
            cnt = max(cnt, (lst[k][j] + lst[k][j+1] + lst[k][j+2] + lst[k][j+3]))
        if (k + 1) < N and (j+1) < M:
            cnt = max(cnt, (lst[k][j] + lst[k][j+1] + lst[k+1][j] + lst[k+1][j+1]))
        if (k + 2) < N and ( j+1 ) < M:
            cnt = max(cnt, (lst[k][j+1] + lst[k+1][j+1] + lst[k+1][j] + lst[k+2][j]))
            cnt = max(cnt, (lst[k][j+1] + lst[k+1][j+1] + lst[k+2][j+1] + lst[k+2][j]))
            cnt = max(cnt, (lst[k][j] + lst[k+1][j] + lst[k][j+1] + lst[k+2][j]))
            cnt = max(cnt, (lst[k][j] + lst[k+1][j] + lst[k+2][j] + lst[k+2][j+1]))
            cnt = max(cnt, (lst[k][j] + lst[k][j+1] + lst[k+1][j+1] + lst[k+2][j+1]))
            cnt = max(cnt, (lst[k][j] + lst[k+1][j] + lst[k+1][j+1] + lst[k+2][j+1]))
            cnt = max(cnt, (lst[k][j] + lst[k+1][j] + lst[k+2][j] + lst[k+1][j+1]))
            cnt = max(cnt, (lst[k][j+1] + lst[k+1][j+1] + lst[k+1][j] + lst[k+2][j+1]))
        if (k + 1) < N and ( j+2 ) < M:
            cnt = max(cnt, (lst[k][j] + lst[k][j+1] + lst[k+1][j+1] + lst[k+1][j+2]))
            cnt = max(cnt, (lst[k][j] + lst[k][j+1] + lst[k][j+2] + lst[k+1][j+2]))
            cnt = max(cnt, (lst[k][j] + lst[k+1][j] + lst[k+1][j+1] + lst[k+1][j+2]))
            cnt = max(cnt, (lst[k][j] + lst[k+1][j] + lst[k][j+1] + lst[k][j+2]))
            cnt = max(cnt, (lst[k+1][j] + lst[k][j+1] + lst[k][j+2] + lst[k+1][j+1]))
            cnt = max(cnt, (lst[k][j] + lst[k][j+1] + lst[k][j+2] + lst[k+1][j+1]))
            cnt = max(cnt, (lst[k][j+1] + lst[k+1][j] + lst[k+1][j+1] + lst[k+1][j+2]))
            cnt = max(cnt, (lst[k+1][j] + lst[k+1][j+1] + lst[k+1][j+2] + lst[k][j+2]))
        
print(cnt)
