# P118667. 두 큐 합 같게 만들기
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/118667


from collections import deque


def solution(queue1, queue2):
    count = 0

    # 시간 복잡도를 위해 list를 deque로 변환
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    # 두 큐의 합
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    # 큐의 길이의 4배까지 반복문 수행
    limit = len(queue1) * 4

    for count in range(0, limit):

        # queue1의 합이 queue2의 합보다 큰 경우
        if sum1 > sum2:

            # queue1에서 원소를 추출하여 queue2에 삽입
            x = queue1.popleft()
            queue2.append(x)

            sum1 = sum1 - x
            sum2 = sum2 + x

        # queue1의 합이 queue2의 합보다 작은 경우
        elif sum1 < sum2:

            # queue2에서 원소를 추출하여 queue1에 삽입
            x = queue2.popleft()
            queue1.append(x)

            sum1 = sum1 + x
            sum2 = sum2 - x

        # queue1의 합괴 queue2의 합이 동일한 경우 반복문 종료
        else:
            return count

    # 반복문을 모두 수행했어도 두 큐의 합이 같지않으면 -1 반환
    return -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))  # 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))    # 7
print(solution([1, 1], [1, 5]))  # -1
