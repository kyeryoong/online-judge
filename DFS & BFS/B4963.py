# B4963. 섬의 개수
# [백준] https://www.acmicpc.net/problem/4963


from collections import deque
import sys
input = sys.stdin.readline


# 재귀 최대 깊이 설정
sys.setrecursionlimit(10000)


# 테스트 케이스 입력
inputs = []

while True:
    x = list(map(int, input().split()))

    if x == [0, 0]:
        break

    else:
        temp = []

        for i in range(0, x[1]):
            temp.append(list(map(int, input().split())))

        inputs.append(temp)


# 메인 함수
def solution(graph):
    n = len(graph)
    m = len(graph[0])

    # 깊이 우선 탐색 알고리즘
    def DFS(x, y):
        if not (0 <= x < n and 0 <= y < m):
            return False

        if graph[x][y] == 1:
            graph[x][y] = graph[x][y] + 1

            # 상, 하, 좌, 우
            DFS(x, y - 1)
            DFS(x, y + 1)
            DFS(x - 1, y)
            DFS(x + 1, y)

            # 좌상, 좌하, 우상, 우하
            DFS(x - 1, y - 1)
            DFS(x - 1, y + 1)
            DFS(x + 1, y - 1)
            DFS(x + 1, y + 1)

            return True

        return False


    # 섬의 개수
    count = 0

    # 섬의 개수가 있는 지점(그래프에서 1인 지점)에서 알고리즘 수행
    for i in range(0, n):
        for j in range(0, m):
            if DFS(i, j):
                count = count + 1

    print(count)


# 테스트 케이스별 메인 함수 수행
for graph in inputs:
    solution(graph)
