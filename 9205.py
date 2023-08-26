# 출발은 상근이네 집에서 맥주 한 박스를 들고 출발
# 한 박스당 20개
# 50m 당 1병


# 전형적인 bfs 문제
# 이제 이정도는 금방 푸는 군하 하하
from collections import deque

T = int(input())


def findFestival(coordinates):
    visited = dict()
    house_x, house_y = coordinates[0]
    Q = deque([(house_x, house_y)])
    while Q:
        x, y = Q.popleft()
        for coordinate in coordinates:
            if abs(coordinate[0] - x) + abs(coordinate[1] - y) <= 1000 and not visited.get(coordinate):
                visited[coordinate] = 1
                Q.append(coordinate)
                if coordinate == coordinates[-1]:
                    print("happy")
                    return 
    return print("sad")



for _ in range(T):
    coordinate = []
    CStore_cnt = int(input())
    for _ in range(CStore_cnt+2):
        coordinate.append((tuple(map(int, input().split()))))

    if abs(coordinate[0][0] - coordinate[-1][0]) + abs(coordinate[0][1] - coordinate[-1][1]) <= 1000:
        print("happy")
        continue
    findFestival(coordinate)
