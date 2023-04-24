# P154540. 무인도 여행
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/154540


import sys
sys.setrecursionlimit(10 ** 7)


def solution(maps):
    # 지도의 크기
    n = len(maps)
    m = len(maps[0])

    for i in range(0, len(maps)):
        maps[i] = list(maps[i])


    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 깊이 우선 탐색 알고리즘
    def DFS(x, y):
        nonlocal count

        count = count + int(maps[x][y])
        
        # 방문한 땅은 "X"로 변경해서 방문 처리
        maps[x][y] = "X"

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            # maps[nx][ny] != "X": 방문하지 않은 곳 또는 바다가 아닌 곳만 방문
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != "X":
                DFS(nx, ny)


    # 각 섬에서 최대로 머무를 수 있는 일 수
    answer = []

    # "X"가 아닌 지점을 모두 방문
    for i in range(0, n):
        for j in range(0, m):
            if maps[i][j] != "X":
                count = 0
                DFS(i, j)
                answer.append(count)

    if answer:
        return sorted(answer)

    else:
        return [-1]


print(solution(["X591X","X1X5X","X231X", "1XXX1"])) # [1, 1, 27]
print(solution(["XXX","XXX","XXX"]))    # [-1]