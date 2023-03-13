# B1932. 정수 삼각형
# [백준] https://www.acmicpc.net/problem/1932


import sys
input = sys.stdin.readline


n = int(input())

triangles = [list(map(int, input().split())) for _ in range(1, n + 1)]

for i in range(1, n):
    # 가장 왼쪽은 대각선 오른쪽을 더함
    triangles[i][0] = triangles[i][0] + triangles[i - 1][0]

    # 가장 왼쪽 또는 오른쪽이 아닌 경우
    for j in range(1, i):

        # 현재 숫자에 대각선 왼쪽과 대각선 오른쪽 중에서 더 큰 것을 더함
        triangles[i][j] = triangles[i][j] + \
            max(triangles[i - 1][j - 1], triangles[i - 1][j])

    # 가장 오른쪽은 대각선 왼쪽을 더함
    triangles[i][i] = triangles[i][i] + triangles[i - 1][i - 1]


# 마지막 층에서 최대값을 출력
print(max(triangles[n - 1]))
