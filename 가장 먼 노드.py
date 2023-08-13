from collections import deque
def solution(n, edge):
    vertex = {i:[] for i in range(0, n)}
    for a, b in edge:
        if not vertex.get(a-1):
            vertex[a-1] = [b-1]
        else:
            vertex[a-1].append(b-1)
        if not vertex.get(b-1):
            vertex[b-1] = [a-1]
        else:
            vertex[b-1].append(a-1)
            
            
    
    distance = [-1] + [0] * (n-1)
    
    visited = [True] + [False] * (n-1)
    Q = deque([(0, 0)])
    max_cnt = 0
    clear = 1
    while Q:
        if clear == n:
            break
        node, cnt = Q.popleft()
        
        for index in vertex.get(node):
            if not visited[index]:
                Q.append((index, cnt+1))
                distance[index] = cnt+1
                visited[index] = True
                max_cnt = max(max_cnt, cnt + 1)
                clear += 1
                
    return distance.count(max_cnt)

# enumerate() -> index와 해당 값이 같이 나타나게 함
# dict.keys() in 하지 말기
