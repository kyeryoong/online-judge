# P42884. 단속카메라
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/42884


def solution(routes):
    # 차량의 진출 지점을 기준으로 정렬
    routes.sort(key=lambda x: x[1])

    # 기준점
    check = -30001

    # 설치해야 하는 카메라의 개수
    answer = 0

    for start, end in routes:
        # [Key Point] 현재 차량의 진입 지점이 기준점보다 뒤에 있으면, 카메라를 새로 설치해야 함
        if start > check:
            # 기준점을 차량의 진출 지점으로 변경            
            check = end
            
            # 카메라의 개수 증가
            answer = answer + 1

    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
