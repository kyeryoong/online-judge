# P12900. 2 x n 타일링
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/12900


def solution(n):
    # 다이내믹 프로그래밍 테이블 초기화
    dp = [0] * (n + 1)

    
    # 첫 번째와 두 번째 값을 추가
    dp[1] = 1
    dp[2] = 2


    # 점화식을 사용하여 세 번째 값 부터 계산
    if n > 2:
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
            
            
    return dp[n]


print(solution(4))  # 5