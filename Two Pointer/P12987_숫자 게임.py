# P12987. 숫자 게임
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/12987


def solution(A, B):
    # 숫자를 오름차순으로 정렬
    A.sort()
    B.sort()

    # B팀이 얻는 승점
    answer = 0

    length = len(A)

    # [Key Point] 투 포인터 사용
    i = 0
    j = 0

    while i < length and j < length:
        # B팀의 숫자가 A팀의 숫자보다 큰 경우
        if A[i] < B[j]:
            i = i + 1
            j = j + 1

            # 승점 추가
            answer = answer + 1

        # A팀의 숫자가 B팀의 숫자보다 큰 경우
        else:
            j = j + 1

    return answer


print(solution([5,1,3,7], [2,2,6,8]))   # 3
print(solution([2,2,2,2], [1,1,1,1]))   # 0
