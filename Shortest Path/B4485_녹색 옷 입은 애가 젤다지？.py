# B4485. 녹색 옷 입은 애가 젤다지?
# [백준] https://www.acmicpc.net/problem/4485


import heapq
import sys
input = sys.stdin.readline


# 무한을 의미하는 값
INF = int(1e9)


# 테스트 케이스 번호
case = 1


# 0이 입력될 때 까지 반복문 수행
while True:
    # 동굴의 크기
    n = int(input())

    if n == 0:
        break

    # 동굴의 각 칸에 있는 도둑 루피의 크기
    graph = [list(map(int, input().split())) for _ in range(0, n)]
    
    
    # 다익스트라 알고리즘
    def dijkstra():
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        # 최소 금액 테이블
        distance = [[INF] * n for _ in range(0, n)]

        # (금액, (x좌표, y좌표)) 형식으로 큐에 삽입
        queue = []
        heapq.heappush(queue, (graph[0][0], (0, 0)))

        while queue:
            min_dist, min_vertex = heapq.heappop(queue)
            min_x, min_y = min_vertex

            # 상하좌우 인접한 곳을 확인
            for i in range(0, 4):
                nx = min_x + dx[i]
                ny = min_y + dy[i]

                # 동굴 안에서만 이동 가능
                if 0 <= nx < n and 0 <= ny < n:
                    cost = min_dist + graph[nx][ny]

                    if cost < distance[nx][ny]:
                        distance[nx][ny] = cost
                        heapq.heappush(queue, (cost, (nx, ny)))

        return distance

    # 제일 오른쪽 아래 칸까지 이동하는데 잃는 최소 금액 출력
    print("Problem %d: %d" % (case, dijkstra()[n - 1][n - 1]))

    case = case + 1
