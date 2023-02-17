# P76502. 괄호 회전하기
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/76502


# 올바른 괄호 문자열인지 확인
def check(words):
    stack = []

    # 여는 괄호가 들어오면, 다음에는 무조건 닫는 괄호가 들어와야 함
    for i in range(0, len(words)):
        if not (stack):
            stack.append(words[i])

        elif stack[-1] == "(" and words[i] == ")":
            stack.pop()

        elif stack[-1] == "[" and words[i] == "]":
            stack.pop()

        elif stack[-1] == "{" and words[i] == "}":
            stack.pop()

        else:
            stack.append(words[i])

    # 스택에 괄호가 남아있으면 올바른 괄호 문자열이 아님
    if stack:
        return False

    else:
        return True


def solution(s):
    answer = 0

    # 괄호 1칸 씩 회전할 때 마다 올바른 괄호 문자열인지 확인
    for i in range(0, len(s)):
        if check(s[i:] + s[0: i]):
            answer = answer + 1

    return answer


print(solution("[](){}"))   # 3
print(solution("}]()[{"))   # 2
print(solution("[)(]"))  # 0
print(solution("}}}"))  # 0
