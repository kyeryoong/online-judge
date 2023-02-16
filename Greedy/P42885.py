# P42885. 구명보트
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/42885


def solution(people, limit):
    people.sort()

    # 투 포인터를 사용하여 가장 가벼운 사람과 가장 무거운 사람을 묶어서 구명보트에 탑승시켜야 함
    front = 0
    rear = len(people) - 1

    answer = 0

    # 투 포인터가 만나기전 까지 실행
    while front <= rear:

        # 가장 가벼운 사람과 가장 무거운 사람의 몸무게 합이 구명 보트의 무게 제한 이하인 경우
        if people[front] + people[rear] <= limit:
            answer = answer + 1

            # 가벼운 사람과 무거운 사람 둘 다 탑승
            front = front + 1
            rear = rear - 1

        # 가장 가벼운 사람과 가장 무거운 사람의 몸무게 합이 구명 보트의 무게 제한을 초과하는 경우
        else:
            answer = answer + 1

            # 무거운 사람만 탑승
            rear = rear - 1

    return answer
