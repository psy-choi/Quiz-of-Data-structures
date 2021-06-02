#내가 쓴 답변

import sys
H, W = map(int, sys.stdin.readline().split())
lst = [[x for x in range(W)]for j in range(H)]
block = list(map(int, sys.stdin.readline().split()))
for i in range(W):
    for j in range(block[i]):
        lst[j][i] = "b"
sum = 0
for i in range(H):
    blocking = []
    cnt = 0
    for j in range(W):
        if len(blocking) == 1:
            cnt += 1
        if lst[i][j] == "b":
            if len(blocking) == 1:
                if lst[i][j-1] == "b":
                    cnt -= 1
                else:
                    sum += (cnt - 1)
                    cnt = 0
            else:
                blocking.append(0)
print(sum)

#다른 곳에서 참조한 답변
import sys
H, W = map(int, sys.stdin.readline().split())
block = list(map(int, sys.stdin.readline().split()))

def trapping_rain(buildings):
    raindrop = 0
    for i in range(len(buildings)):
        # 현재 인덱스의 왼쪽에서 가장 높은 건물의 높이
        max_left = max(buildings[:i+1])  #자신을 포함함
        # 현재 인덱스의 오른쪽에서 가장 높은 건물의 높이
        max_right = max(buildings[i:])
        # 둘중에 어떤 값이 더 작은가?
        which_low = min(max_left, max_right)
        # 절대값 주의
        raindrop = raindrop + abs(buildings[i] - which_low)
    return raindrop

print(trapping_rain(block))

#이렇게 짧게 할 수 있는 것을 저렇게 풀었다..2차원으로만 생각하지 말 것!
