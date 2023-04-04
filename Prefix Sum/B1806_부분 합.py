# B1806. 부분합
# [백준] https://www.acmicpc.net/problem/1806


import sys
input = sys.stdin.readline


# 수열의 길이와 합 S
n, s = map(int, input().split())

# 수열
numbers = list(map(int, input().split()))

# prefix_sum[i]: 첫 번째 자연수부터 i 번째 자연수까지의 합
prefix_sum = [0]

for i in range(0, n):
    prefix_sum.append(prefix_sum[i] + numbers[i])

# [Key Point] 투 포인터 사용
left = 0
right = 0

# 연속된 수들의 부분합이 s 이상 되는 것 중, 가장 짧은 것의 길이
answer = int(1e9)

while right < n:
    # check: left 번째 자연수부터 right 번째 자연수까지의 합
    check = prefix_sum[right + 1] - prefix_sum[left]

    # 수열의 길이
    length = right - left + 1

    # [Key Point] 수열의 합이 s보다 작으면, right를 오른쪽으로 이동
    if check < s:
        right = right + 1

    # [Key Point] 수열의 합이 s보다 크면, left를 오른쪽으로 이동
    if check >= s:
        left = left + 1

        answer = min(answer, length)


# 합을 만드는 것이 가능한 경우
if answer != int(1e9):
    print(answer)

# 합을 만드는 것이 불가능한 경우
else:
    print(0)
