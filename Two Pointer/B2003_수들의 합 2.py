# B2003. 수들의 합 2
# [백준] https://www.acmicpc.net/problem/2003


import sys
input = sys.stdin.readline

# 수열의 길이와 합 M
n, m = map(int, input().split())

# 수열
numbers = list(map(int, input().split()))

# 투 포인터
left = 0
right = 0

# 수열 A[left] ~ A[right] 까지의 합
total = numbers[0]

# 경우의 수
answer = 0


while True:
    # 수열의 합이 M보다 작은 경우: 다음 숫자 추가
    if total < m:
        right = right + 1
        
        if right == n:
            break
        
        total = total + numbers[right]

    # 수열의 합이 M보다 큰 경우: 맨 왼쪽 숫자 제거
    elif total > m:
        total = total - numbers[left]
        left = left + 1

    # 수열의 합이 M과 같은 경우: 맨 왼쪽 숫자 제거
    else:
        answer = answer + 1

        total = total - numbers[left]
        left = left + 1


print(answer)
