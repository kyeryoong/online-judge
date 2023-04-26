# B1253. 좋다
# [백준] https://www.acmicpc.net/problem/1253


import sys
input = sys.stdin.readline


# 수의 개수
n = int(input())

# 숫자들
numbers = list(map(int, input().split()))
numbers.sort()


# 좋은 수의 개수
answer = 0


# 모든 수를 처음부터 끝까지 확인
for i in range(0, n):
    # 투 포인터 사용
    left = 0
    right = n - 1

    # 확인 할 숫자 (= 어떤 수)
    x = numbers[i]

    while left < right:
        # [Key Point] c = a + b를 만족해야 하는 과정에서, a와 b는 c랑 다른 수여야 한다.
        # 단, a와 b가 c와 같은 값이여도, 위치가 다르면 다른 수 이다.

        # left 포인터에 있는 숫자가 확인 할 숫자면 생략
        if left == i:
            left = left + 1
            continue

        # right 포인터에 있는 숫자가 확인 할 숫자면 생략
        if right == i:
            right = right - 1
            continue

        # 두 수의 합
        total = numbers[left] + numbers[right]

        # 합이 X보다 작은 경우: 왼쪽 포인터 증가(= 두 수의 합을 증가)
        if total < x:
            left = left + 1

        # 합이 X보다 큰 경우: 오른쪽 포인터 감소(= 두 수의 합을 감소)
        elif total > x:
            right = right - 1

        # 합이 X와 같은 경우: while 반복문 종료
        elif total == x:
            answer = answer + 1
            break


print(answer)
