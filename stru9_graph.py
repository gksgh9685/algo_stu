# 깊이 우선 탐색 방식 - 재귀 또는 스택으로 구현 - 경로 추적, 백트레킹에 적합

def dfsFunc(graph, start, visited):
    visited.append(start)
    for next_node in graph[start]:
        if next_node not in visited:
            dfsFunc(graph, next_node, visited)


visited_bfs = []
dfsFunc(graph,'A',visited_bfs)
print('DFS 방문 순서 : ',visited_bfs)


print()
# BFS : 너비 우선 탐색 방식 -Queue로 구현 - 최단 거리 탐색에 적합
from collections import deque
def bfsFunc(graph, start):
    visited = [start]
    queue = deque([start])

    while queue: 
        node = queue.popleft()
        for next_node in graph[node]:
            if next_node not in visited:
                visited.append(next_node) # 방문 처리
                queue.append(next_node) # 다음 탐색 대상으로 큐

    return visited

visited_bfs = bfsFunc(graph, 'A')
print('BFS 방문 순서 : ', visited_bfs)