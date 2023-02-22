# P131704. 두 큐 합 같게 만들기
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/131704


def solution(order):
    # 보조 컨테이너 벨트
    stack = []

    i = 1

    # 현재 배달 순서
    order_index = 0

    for i in range(1, len(order) + 1):    
        
        # 컨테이너 벨트에서 택배 상자를 꺼내 보조 컨테이너 벨트로 삽입
        stack.append(i)

        # 보조 컨테이너 벨트의 가장 마지막 택배 상자가 현재 배달 순서랑 일치하는지 확인
        while stack and stack[-1] == order[order_index]:
            order_index = order_index + 1

            stack.pop()


    return order_index


print(solution([4, 3, 1, 2, 5]))    # 2
print(solution([5, 4, 3, 2, 1]))    # 5
    