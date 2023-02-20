# P17684. 전화번호 목록
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/17684


def solution(msg):
    # 길이가 1인 모든 단어를 포함하도록 사전을 초기화
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictionary = {alphabet[i] : i + 1 for i in range(0, len(alphabet))}

    # 문자열 탐색 포인터
    idx = 0

    answer = []

    while idx < len(msg):
        w = ""

        # 사전에서 현재 입력과 일치하는 가장 긴 문자열 찾기
        for j in range(0, len(msg) - idx):
            
            # 사전에 있는 가장 긴 문자열(w)을 찾았으면 색인 번호 출력
            if msg[idx : idx + j + 1] in dictionary:
                w = msg[idx : idx + j + 1]

            # 가장 긴 문자열(w)와 다음 글자(c)를 추가한 w+c를 사전에 등록
            else:
                dictionary[msg[idx : idx + j + 1]] = len(dictionary) + 1
                break

        answer.append(dictionary[w])

        # 가장 긴 문자열의 길이만큼 포인터 이동
        idx = idx + len(w)

    return answer


print(solution("KAKAO"))    # [11, 1, 27, 15]
print(solution("TOBEORNOTTOBEORTOBEORNOT")) # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print(solution("ABABABABABABABAB"))  # [1, 2, 27, 29, 28, 31, 30]
