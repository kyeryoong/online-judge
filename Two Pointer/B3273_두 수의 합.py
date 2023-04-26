# B3273. 두 수의 합
# [백준] https://www.acmicpc.net/problem/3273


import sys
input = sys.stdin.readline


# 수열의 길이
n = int(input())

# 수열
numbers = list(map(int, input().split()))
numbers.sort()

# 자연수 X
x = int(input())


# 투 포인터
left = 0
right = n - 1

# (ai, aj)쌍의 수
answer = 0


# 왼쪽 포인터가 오른쪽 포인터보다 작을 때 까지 반복문 수행
while left < right:
    # 두 수의 합
    total = numbers[left] + numbers[right]

    # 합이 X보다 작은 경우: 왼쪽 포인터 증가(= 두 수의 합을 증가)
    if total < x:
        left = left + 1

    # 합이 X보다 큰 경우: 오른쪽 포인터 감소(= 두 수의 합을 감소)
    elif total > x:
        right = right - 1

    # 합이 X와 같은 경우: 오른쪽 포인터 감소(= 두 수의 합을 감소)
    elif total == x:
        answer = answer + 1
        right = right - 1


print(answer)
