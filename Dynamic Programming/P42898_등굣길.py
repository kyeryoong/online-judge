# P42898. 등굣길
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/42898


def solution(m, n, puddles):
    # dp[i][j]: 집(1, 1)에서 해당 지점(i, j)까지 갈 수 있는 최단경로의 개수
    dp = [[0] * (m + 1) for _ in range(0, n + 1)]

    # 물이 담긴 지역은 -1로 표시
    for y, x in puddles:
        dp[x][y] = -1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 집 (1, 1)은 1로 초기화
            if i == 1 and j == 1:
                dp[i][j] = 1

            else:
                # 물이 담긴 지역은 해당 지점으로 갈 수 없기 때문에, 0으로 설정
                if dp[i][j] == -1:
                    dp[i][j] = 0

                # [Key Point] 해당 지점(i, j)으로 갈 수 있는 최단경로 개수 = (해당 지점 바로 위쪽 지점(i - 1, j)으로 갈 수 있는 최단경로 개수) + (해당 지점 바로 왼쪽 지점(i, j - 1)으로 갈 수 있는 최단경로 개수)
                # 최단경로의 개수를 1,000,000,007로 나눠야 하는 조건 추가
                else:
                    dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    return dp[n][m]


print(solution(4, 3, [[2, 2]]))  # 4
