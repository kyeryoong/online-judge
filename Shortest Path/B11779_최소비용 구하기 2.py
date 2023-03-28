# B1916. 최소비용 구하기 2
# [백준] https://www.acmicpc.net/problem/11779


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


def dijkstra(vertex):
    # 최단 거리 테이블
    distance = [INF] * (n + 1)
    distance[0] = 0
    
    # [Key Point] 최단 거리로 가는 경로가 담긴 테이블
    answer = [None] * (n + 1)

    queue = []
    
    # (거리, 도시, 도시까지 가는 경로) 형식으로 큐에 삽입
    heapq.heappush(queue, (0, vertex, [vertex]))

    while queue:
        # 최단 거리가 가장 짧은 도시의 (거리, 정점, 도시까지 가는 경로)를 꺼내기
        min_dist, min_vertex, min_routes = heapq.heappop(queue)

        if distance[min_vertex] < min_dist:
            continue

        # 현재 도시와 연결된 다른 인접한 도시들을 확인
        for v, d in graph[min_vertex]:
            cost = min_dist + d

            # 현재 도시를 거쳐서 다른 도시로 이동하는 거리가 더 짧은 경우 
            if cost < distance[v]:
                distance[v] = cost
                answer[v] = min_routes + [v]
                
                # [Key Point] min_routes + [v]: 도시까지 가는 경로에 현재 도시를 추가
                heapq.heappush(queue, (cost, v, min_routes + [v]))

    return distance, answer


# 출발점에서 다익스트라 알고리즘 수행
distance, answer = dijkstra(start)


# 도착점까지 가는데 드는 최소 비용 출력
print(distance[end])

# 도착점까지 가는 경로에 포함되어있는 도시의 개수
print(len(answer[end]))

# 도착점까지 가는 경로에 포함되어있는 도시를 순서대로 출력
print(*answer[end])
