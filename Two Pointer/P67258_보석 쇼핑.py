# P67258. 보석 쇼핑
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/67258


def solution(gems):
    # 보석 종류 가짓 수
    gems_type = len(set(gems))
    
    # 구간에 담긴 보석
    cart = {}
    
    # 시작 번호와 끝 번호
    left = 0
    right = 0
    
    # 정답
    answer = []

    # 보석 진열대의 마지막까지 탐색
    while right < len(gems):
        # 구간에 모든 종류의 보석이 담길 때 까지, 끝 번호를 증가
        if gems[right] in cart:
            cart[gems[right]] = cart[gems[right]] + 1

        else:
            cart[gems[right]] = 1

        right = right + 1


        # 구간에 모든 종류의 보석이 담겼으면, 시작 번호를 증가
        # 단, 시작점을 증가한 후, 모든 종류의 보석 중 하나라도 포함되지 않으면 중단
        while len(cart) == gems_type:
            if cart[gems[left]] == 1:
                del cart[gems[left]]

            else:
                cart[gems[left]] = cart[gems[left]] - 1

            left = left + 1

            answer.append([left, right])
            
    # x[1] - x[0]: 가장 짧은 구간을 선택
    # x[0]: 가장 짧은 구간이 여러 개면, 시작 번호가 가장 작은 것을 선택
    answer.sort(key=lambda x: (x[1] - x[0], x[0]))

    return answer[0]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA",
      "EMERALD", "SAPPHIRE", "DIA"]))    # [3, 7]
print(solution(["AA", "AB", "AC", "AA", "AC"]))  # [1, 3]
print(solution(["XYZ", "XYZ", "XYZ"]))  # [1, 1]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))   # [1, 5]
