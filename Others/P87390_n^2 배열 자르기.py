# P87390. n^2 배열 자르기
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/87390


def solution(n, left, right):
    answer = []
        
    for i in range(left, right + 1):
        
        # n번째 숫자의 행은 i // n
        row = i // n
        
        # n번째 숫자의 열은 i % n
        column = i % n
        
        # n번째 숫자 = (행과 열 중에서 큰 것) + 1
        answer.append(max(row, column) + 1)
    
    return answer


print(solution(3, 2, 5))
print(solution(4, 7, 14))
