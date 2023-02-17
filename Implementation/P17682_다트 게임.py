# P17682. 다트 게임
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/17682


def solution(dartResult):
    splited = []

    # 10점을 처리하기 위해 문자열 "10"을 "X"로 치환
    dartResult = dartResult.replace("10", "X")


    # dartResult 문자열을 분할
    start = 0

    for end in range(1, len(dartResult)):
        if dartResult[end].isdigit() or dartResult[end] == "X":
            splited.append(list(dartResult[start: end]))

            start = end

    splited.append(list(dartResult[start:]))
    
    for i in range(0, len(splited)):
        if len(splited[i]) == 2:
            if splited[i][0].isdigit():
                splited[i] = [int(splited[i][0]), splited[i][1], ""]

            else:
                splited[i] = [10, splited[i][1], ""]

        else:
            if splited[i][0].isdigit():
                splited[i] = [int(splited[i][0]), splited[i][1], splited[i][2]]

            else:
                splited[i] = [10, splited[i][1], splited[i][2]]


    # 각 기회의 점수
    answer = []
    
    # 보너스
    bonus_dict = {"S": 1, "D": 2, "T": 3}

    # 각 기회마다 계산
    for i in range(0, len(splited)):
        score, bonus, option = splited[i]

        current = score ** bonus_dict[bonus]
        
        # 옵션이 스타상인 경우
        if option == "*":
            current = current * 2
            
            try:
                answer[i - 1] = answer[i - 1] * 2
                
            except:
                pass
            
        # 옵션이 아차상인 경우
        if option == "#":
            current = current * -1
                    
        answer.append(current)


    # 각 기회의 점수를 합산
    return sum(answer)


print(solution("1S2D*3T"))  # 37
print(solution("1D2S#10S")) # 9
print(solution("1D2S0T"))   # 3
print(solution("1S*2T*3S")) # 23
print(solution("1D#2S*3S")) # 5
print(solution("1T2D3D#"))  # -4
print(solution("1D2S3T*"))  # 59
