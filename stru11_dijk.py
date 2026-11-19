import heapq

graph = { # 무방향 형태
    'A':[('B',1),('C',4)],
    'B':[('A',1),('C',1),('D',2)],
    'C':[('A',4),('B',1),('D',3)],
    'D':[('B',2),('C',3)]   
}

def dijkstraFunc(graph, start):
    dist = {node:float('inf') for node in graph}  # 모든 노드까지의 최단 거리를 무한대
    dist[start] = 0  # 'A' = 0   확정된 최단 거리만 기억
    print(dist)  # {'A': 0, 'B': inf, 'C': inf, 'D': inf}

    pq = [(0, start)] # (현재까지의거리, 노드) : 후보 목록 (갈 수 있는 모든 경로)

    while pq:
        cur_dist, u = heapq.heappop(pq)   # Min Heap (Greedy한 선택)
        if cur_dist > dist[u]:  # 더 짧은 경로가 있다면 현재 노드는 무시(중복 방지)
            continue

        for v, w in graph[u]: # 현재 노드(u)와 연결된 이웃 노드 ㅍ xkator
            new_dist = cur_dist + w # u를 거쳐 v로 가는 새 노드의 거리를 계산
            if new_dist < dist[v]:
                dist[v] = new_dist  # 최단 거리 저장소(최단 거리로 갱신)
                heapq.heappush(pq, (new_dist, v))   # 최단 거리로 큐(Min Heap)에 삽입
    return dist


print(dijkstraFunc(graph, 'A'))