# P148653. 마법의 엘리베이터
# [백준] https://school.programmers.co.kr/learn/courses/30/lessons/148653


import math


# n번째 자리에서 내림하는 함수
def roundDown(number, n):
    return math.floor(number / 10 ** n) * 10 ** n

# n번째 자리에서 올림하는 함수
def roundUp(number, n):
    return math.ceil(number / 10 ** n) * 10 ** n


def solution(storey):
    # 0층으로 가기 위해 사용한 마법의 돌의 개수
    answer = []

    # 최소 층수: storey가 n자리 인 경우, n번째 자리에서 내림한 정수
    # 최대 층수: storey가 n자리 인 경우, n번째 자리에서 올림한 정수
    limit_a = roundDown(storey, len(str(storey)))
    limit_b = roundUp(storey, len(str(storey)))

    # 깊이 우선 탐색 알고리즘
    # 현재 층수, 내림/올림하는 자릿수, 현재 사용한 마법의 돌의 개수
    def DFS(number, digit, count):
        # 아랫층과 윗층
        a = roundDown(number, digit)
        b = roundUp(number, digit)

        # 아랫층 또는 윗층으로 이동 시, 필요한 마법의 돌의 개수
        diff_a = abs(a - number) // (10 ** (digit - 1))
        diff_b = abs(b - number) // (10 ** (digit - 1))

        # 0층 도달 시, 탐색 종료
        if number == 0:
            answer.append(count)
            return

        # 최대 층수 초과 시, 탐색 종료
        if number > max(limit_a, limit_b):
            return

        # 아랫층으로 이동
        DFS(a, digit + 1, count + diff_a)
        
        # 윗층으로 이동
        DFS(b, digit + 1, count + diff_b)


    DFS(storey, 1, 0)

    # 0층으로 가기 위해 사용한 마법의 돌의 개수 중 최소값을 반환
    return min(answer)


print(solution(16)) # 6
print(solution(2554))   # 16
    