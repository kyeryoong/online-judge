# B2156. 트리
# [백준] https://www.acmicpc.net/problem/2156


import sys
input = sys.stdin.readline



n = int(input())

wines = [int(input()) for _ in range(0, n)]


# dp[i]: i번째 잔 까지 마실 수 있을 때 최대로 마실 수 있는 포도주 양
dp = [0] * n

# 첫 번째 잔만 마실 수 있는 경우 최대값 = (첫 번째 잔)
dp[0] = wines[0]

# 두 번째 잔까지 마실 수 있는 경우 최대값 = (첫 번째 잔) + (두 번째 잔)
dp[1] = dp[0] + wines[1]

if n > 2:
    for i in range(2, n):
        # 이번 잔(i)을 마시고, 이전 잔(i - 1)은 마시지 않는 경우
        case1 = dp[i - 2] + wines[i]
        
        # 이번 잔(i), 이전 잔(i - 1)을 마시고, 전전 잔(i - 2)은 마시지 않는 경우
        case2 = dp[i - 3] + wines[i - 1] + wines[i]
        
        # 이번 잔(i)을 마시지 않는 경우
        case3 = dp[i - 1]
        
        dp[i] = max(case1, case2, case3)


print(dp[n - 1])
