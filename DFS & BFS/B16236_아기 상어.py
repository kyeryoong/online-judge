# B16236. 아기 상어
# [백준] https://www.acmicpc.net/problem/16236


from collections import deque
import sys
input = sys.stdin.readline


# 무한을 의미하는 값
INF = int(1e9)


# 공간의 크기
n = int(input())

# 공간의 상태
graph = [list(map(int, input().split())) for _ in range(0, n)]


# 아기 상어의 크기
size = 2

# 아기 상어의 현재 위치
x, y = 0, 0

# 아기 상어의 처음 위치
for i in range(0, n):
    for j in range(0, n):
        if graph[i][j] == 9:
            x, y = i, j


# 아기 상어가 먹을 수 있는 물고기를 확인
def BFS(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(x, y)])

    # 각 위치 방문 여부
    visited = [[False] * n for _ in range(0, n)]

    # 아기 상어의 현재 위치는 0으로 초기화
    visited[x][y] = 1

    # 각 위치까지의 거리
    distance = [[0] * n for _ in range(0, n)]

    # 먹을 수 있는 물고기가 담긴 리스트
    target = []

    while queue:
        x, y = queue.popleft()

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            # graph[nx][ny] <= size: 아기 상어는 자신보다 크기가 작거나 같은 물고기로 이동할 수 있음
            # not visited[nx][ny]: 방문하지 않은 곳으로 이동할 수 있음
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] <= size and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1

                # 아기 상어는 자신보다 크기가 작은 물고기를 먹을 수 있음
                if 1 <= graph[nx][ny] < size:
                    target.append((nx, ny, distance[nx][ny]))


    # 먹을 수 있는 물고기가 있는 경우
    if len(target) > 0:
        # 거리가 가까운 물고기가 많으면, 가장 위에 있는 물고기와 가장 왼쪽에 있는 물고기를 먹음

        # x[2]: 거리, x[0]: 위~아래 위치, x[1]: 왼쪽~오른쪽 위치
        # 우선순위: 거리 -> 위~아래 -> 왼쪽~오른쪽
        return sorted(target, key=lambda x: (-x[2], -x[0], -x[1]), reverse=True)[0]

    # 먹을 수 있는 물고기가 없는 경우
    else:
        return False


# 아기 상어 이동 거리
answer = 0

# 아기 상어가 현재 잡아먹은 물고기 수
eaten = 0


# 먹을 수 있는 물고기가 있을 때 까지 반복문 수행
while True:
    check = BFS(x, y)

    # 먹을 수 있는 물고기가 없는 경우
    if not check:
        print(answer)
        break

    # 먹을 수 있는 물고기가 있는 경우
    else:
        # target_x, target_y: 먹을 수 있는 물고기의 위치
        # distance: 먹을 수 있는 물고기 까지의 거리
        target_x, target_y, distance = check
        
        # 잡아 먹은 물고기의 위치는 0으로 변경
        graph[target_x][target_y] = 0
            
        # 현재 위치에서 먹을 수 있는 물고기의 위치로 이동
        graph[x][y] = 0
        x, y = target_x, target_y

        # 이동거리 증가
        answer = answer + distance

        # 잡아먹은 물고기 수 증가
        eaten = eaten + 1

    # 아기 상어가 자신의 크기와 같은 수의 물고기를 먹을 때 크기가 1 증가
    if eaten == size:
        size = size + 1
        eaten = 0
