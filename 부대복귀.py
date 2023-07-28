#프로그래머스 LV3
#다익스트라 or BFS



# this code for dikstra
def dikstra(n, member_point, destination, road):
    distance = [100001 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    distance[member_point] = 0
    visited[member_point] = True

    while not visited[destination]:
        standard_distance = 100001
        main_point = member_point
        for point in road[member_point]:
            distance[point] = min(distance[point], distance[main_point]+1)
            if not visited[point] and standard_distance >= distance[point]:
                standard_distance = distance[point]
                member_point = point
        if member_point == destination:
            break
        if visited[member_point]:
            break
        visited[member_point] = True
        
    if distance[destination] == 100001:
        return -1
    else:
        return distance[destination]

def solution(n, roads, sources, destination):
    road = [[] for _ in range(n+1)]
    for x,y in roads:
        road[x].append(y), road[y].append(x)
    answer = []
    for source in sources:
        answer.append(dikstra(n, source, destination, road))
  
    return answer







# this code for BFS
from collections import deque

def solution(n, roads, sources, destination):
    visited = [-1] * (n+1)
    road = [[] for i in range(n+1)]
    for x,y in roads:
        road[x].append(y)
        road[y].append(x)
    
    Q = deque([destination])
    visited[destination] = 0
    while Q:
        point = Q.popleft()
        for connected_point in road[point]:
            if visited[connected_point] == -1:
                visited[connected_point] = visited[point] + 1
                Q.append(connected_point)

    return [visited[i] for i in sources]
