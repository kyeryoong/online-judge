# P67256. 키패드 누르기
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/67256


# 현재 손가락에서 키패드까지 거리 계산
def getDistance(left, right, target, hand):
    ld = abs(target[0] - left[0]) + abs(target[1] - left[1])
    rd = abs(target[0] - right[0]) + abs(target[1] - right[1])

    # 오른손 엄지손가락이 더 가까운 경우
    if ld > rd:
        return "right"

    # 왼손 엄지손가락이 더 가까운 경우
    elif ld < rd:
        return "left"

    # 거리가 동일하면 주 손가락을 사용
    elif ld == rd:
        return hand


def solution(numbers, hand):
    # 키패드의 위치
    key = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        "*": [3, 0], 0: [3, 1], "#": [3, 2]
    }
    

    # 현재 왼손과 오른쪽 엄지손가락의 위치
    l = key["*"]
    r = key["#"]

    answers = ""

    for number in numbers:
        
        # 1, 4, 7을 입력하는 경우 = 왼손 엄지손가락을 사용
        if number in [1, 4, 7]:
            l = key[number]
            answers = answers + "L"

        # 3, 6, 9을 입력하는 경우 = 오른손 엄지손가락을 사용
        elif number in [3, 6, 9]:
            r = key[number]
            answers = answers + "R"

        # 2, 5, 8, 0을 입력하는 경우
        else:
            
            # 왼손 엄지손가락을 사용하는 경우
            if getDistance(l, r, key[number], hand) == "left":
                l = key[number]
                answers = answers + "L"
                
            # 오른손 엄지손가락을 사용하는 경우
            else:
                r = key[number]
                answers = answers + "R"


    return answers


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
