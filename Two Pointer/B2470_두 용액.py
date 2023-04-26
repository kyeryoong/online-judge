# B2470. 두 용액
# [백준] https://www.acmicpc.net/problem/2470


import sys
input = sys.stdin.readline


INF = int(1e9)

# 용액의 수
n = int(input())

# 용액
liquids = list(map(int, input().split()))
liquids.sort()


# 투 포인터
left = 0
right = n - 1

# 특성값이 0에 가장 가까운 두 용액
answer = (INF, INF)


# 왼쪽 포인터가 오른쪽 포인터보다 작을 때 까지 반복문 수행
while left < right:
    # 새로 만든 용액의 특성값
    total = liquids[left] + liquids[right]

    # 새로 만든 용액의 특성값이 이전 용액의 특성값보다 0에 가까운 경우
    if abs(total) < abs(sum(answer)):
        answer = (liquids[left], liquids[right])

        # 새로 만든 용액의 특성값이 0인 경우: 반목문 종료
        if total == 0:
            break

    # 새로 만든 용액의 특성값이 0보다 큰 경우: 오른쪽 포인터 감소(= 두 용액의 합을 감소)
    if total > 0:
        right = right - 1

    # 새로 만든 용액의 특성값이 0보다 작은 경우: 왼쪽 포인터 감소(= 두 용액의 합을 증가)
    elif total < 0:
        left = left + 1


print(answer[0], answer[1])
