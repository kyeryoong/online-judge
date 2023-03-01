# B14501. 퇴사
# [백준] https://www.acmicpc.net/problem/14501


n = int(input())

schedule = [list(map(int, input().split())) for _ in range(0, n)]


# dp[i]: i일에 받을 수 있는 금액의 최댓값
dp = [0] * (n + 1)


for i in range(0, n):
    start = i   # 상담 시작일
    finish = i + schedule[i][0] # 상담 종료일
    pay = schedule[i][1]  # 상담 종료 시 받을 수 있는 금액
    
    # 상담 종료일이 퇴사일 이내에 있는지 확인
    if finish <= n:
        # (기존 상담 종료일에 받을 수 있는 금액의 최댓값)과 (상담 시작일에 받을 수 있는 금액의 최댓값 + 이번 상담을 진행할 경우 받을 수 있는 금액)을 비
        dp[finish] = max(dp[finish], dp[i] + pay)

    # 오늘 일할 수 없다면, 어제까지 일했을 때 얻은 금액을 넣어줌
    dp[i + 1] = max(dp[i + 1], dp[i])

print(max(dp))
