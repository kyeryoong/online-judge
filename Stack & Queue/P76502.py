# P76502. 괄호 회전하기
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/76502


# 올바른 괄호 문자열인지 확인
def check(words):
    stack = []
    
    for i in range(0, len(words)):
        if not(stack):
            stack.append(words[i])
            
        elif stack[-1] == "(" and words[i] == ")":
            stack.pop()
                
        elif stack[-1] == "[" and words[i] == "]":
            stack.pop()
                
        elif stack[-1] == "{" and words[i] == "}":
            stack.pop()
                
        else:
            stack.append(words[i])
                
    if stack:
        return False
    
    else:
        return True
    
            
def solution(s):
    answer = 0
    
    # 괄호 1칸 씩 회전할 때 마다 올바른 괄호 문자열인지 확인
    for i in range(0, len(s)):
        if check(s[i : ] + s[0 : i]):
            answer = answer + 1
            
    return answer


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))