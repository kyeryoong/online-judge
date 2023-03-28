# B1916. 최소비용 구하기
# [백준] https://www.acmicpc.net/problem/1916


import heapq
import sys
input = sys.stdin.readline


# 무한을 의미하는 값
INF = int(1e9)


# 도시와 버스의 개수
n = int(input())
m = int(input())

# 각 도시에 연결되어 있는 버스에 대한 정보
graph = [[] for _ in range(0, n + 1)]


# 버스 정보 입력
for _ in range(0, m):
    # a 도시에서 b 도시로 가는 비용은 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 출발점과 도착점
start, end = map(int, input().split())

    
def dijkstra(start):
    # 최단 거리 테이블
    distance = [INF] * (n + 1)
    distance[start] = 0
    
    queue = []
    
    # 출발점으로 가기 위한 최단 경로를 0으로 설정한 후 큐에 삽입
    heapq.heappush(queue, (0, start))

        # 큐가 비어있지 않는 동안 수행
    while queue:
        # 최단 거리가 가장 짧은 노드의 정보 꺼내기 
        dist, now = heapq.heappop(queue)
        
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
                
    return distance


# 출발점에서 다익스트라 알고리즘 수행
distance = dijkstra(start)


# 도착점까지 가는데 드는 최소 비용 출력
print(distance[end])
