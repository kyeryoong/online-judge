# B16234. 연결 요소의 개수
# [백준] https://www.acmicpc.net/problem/16234


from collections import deque
import sys
input = sys.stdin.readline


# 땅의 크기, 인구 차이 최소 기준, 인구 차이 최대 기준
n, l, r = list(map(int, input().split()))

# 각 나라의 인구수 배열
population = [list(map(int, input().split())) for _ in range(0, n)]


# 너비 우선 탐색 알고리즘
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS(x, y):
    queue = deque([(x, y)])

    # 연합 국가 배열
    result = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 인구 차이: abs(population[nx][ny] - population[x][y])
            # 인구 차이가 l 이상 r 이하이면 연합 국가
            if 0 <= nx < n and 0 <= ny < n and not (visited[nx][ny]) and l <= abs(population[nx][ny] - population[x][y]) <= r:
                queue.append((nx, ny))
                result.append((nx, ny))

                visited[nx][ny] = True

    # 연합 국가의 배열을 반환
    return list(result)


# 인구 이동일
answer = 0

while True:
    # 각 나라 방문 여부
    visited = [[False] * n for _ in range(0, n)]

    # 인구 이동 여부
    modified = False

    # 방문하지 않은 모든 나라를 방문하여 연합 국가인지 확인
    for i in range(0, n):
        for j in range(0, n):
            if not (visited[i][j]):
                visited[i][j] = True

                adjacent = BFS(i, j)

                # adjacent의 값이 2개 이상이면 연합 국가
                # 연합 국가가 있으면 인구 이동 수행
                if len(adjacent) > 1:
                    # 연합 국가의 모든 인구수
                    total = sum([population[x][y] for x, y in adjacent])

                    # 인구 이동 실시(연합 국가의 인구수를 변경)
                    modified = True

                    for x, y in adjacent:
                        population[x][y] = total // len(adjacent)

    # 인구 이동이 되지 않았으면 반복문 중단
    if not (modified):
        break

    # 인구 이동이 되었으면 인구이동일 증가
    else:
        answer = answer + 1


# 인구 이동일 출력
print(answer)
