# P12936. 줄 서는 방법
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/12936


from math import factorial


def solution(n, k):
    answer = []

    # 1번부터 n번까지 번호
    numbers = [i for i in range(1, n + 1)]

    # [Key Point] i번째 자리 숫자 = numbers[x] (1 <= i <= n)
    for _ in range(0, n):
        x = (k - 1) % factorial(len(numbers)) // factorial(len(numbers) - 1)
        answer.append(numbers[x])
        
        # i번째 자리 숫자 제거
        numbers.remove(numbers[x])

    return answer


print(solution(3, 5))   # [3, 1, 2]
