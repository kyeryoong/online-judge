# B11053. 가장 긴 증가하는 부분 수열
# [백준] https://www.acmicpc.net/problem/11053


import sys
input = sys.stdin.readline


n = int(input())

numbers = list(map(int, input().split()))


# dp[i]: i번째 숫자를 마지막으로 했을 때 가장 긴 증가하는 부분 수열의 길이
dp = [1] * n


for i in range(0, n):
    for j in range(0, i):
        # i번째 숫자가 j번째 숫자보다 크면
        # dp[i]와 dp[j](j번째 숫자를 마지막으로 했을 때 가장 긴 증가하는 부분 수열의 길이) + 1을 비교해서 큰 값을 선택
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))
