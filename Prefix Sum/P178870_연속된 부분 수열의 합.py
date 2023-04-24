# P178870. 연속된 부분 수열 합
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/178870


def solution(sequence, k):
    # [Key Point] 투 포인터 사용
    left = 0
    right = 0

    # 부분 수열 합: 수열의 시작 인덱스부터 마지막 인덱스까지의 합
    total = sequence[0]

    # 수열의 시작 인덱스와 마지막 인덱스의 배열을 담는 배열
    answer = []

    while right < len(sequence):
        # 부분 수열 합이 k보다 작은 경우: 마지막 인덱스 뒤에 있는 숫자를 추가
        if total < k:
            right = right + 1

            if right < len(sequence):
                total = total + sequence[right]

        # 부분 수열 합이 k보다 큰 경우: 시작 인덱스의 숫자를 제거
        elif total > k:
            total = total - sequence[left]
            left = left + 1

        # 부분 수열 합이 k와 일치하는 경우: answer에 시작과 마지막 인덱스를 추가
        elif total == k:
            answer.append([left, right])
            total = total - sequence[left]
            left = left + 1

    # x[1] - x[0]: 길이가 짧은 수열을 우선
    # x[0]: 길이가 짧은 수열이 여러 개인 경우 시작 인덱스가 작은 수열을 우선
    answer.sort(key=lambda x: (x[1] - x[0], x[0]))

    return answer[0]
