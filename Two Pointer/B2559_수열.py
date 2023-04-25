# B2559. 수열
# [백준] https://www.acmicpc.net/problem/2559


import sys
input = sys.stdin.readline


# 수열의 길이와 숫자 K
n, k = map(int, input().split())

# 수열
numbers = list(map(int, input().split()))


# 투 포인터
left = 0
right = k

# 연속적인 K일의 온도의 합
total = sum(numbers[left : right])

# 최대값
answer = total

# 마지막날 까지 반복문 수행
while right < n:
    # K일 중, 첫째 날을 빼고, 다음 날을 더함
    total = total - numbers[left] + numbers[right]

    # 투 포인터 이동
    left = left + 1
    right = right + 1

    # 최대값 확인
    answer = max(total, answer)


print(answer)
