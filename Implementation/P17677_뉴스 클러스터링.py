# P17677. 뉴스 클러스터링
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/17677


from collections import Counter

def solution(str1, str2):
    arr1 = []
    arr2 = []
    
    # 두 글자씩 끊어서 영문자로 된 글자 쌍만 다중집합에 삽입
    # [Key Point] 다중 집합은 중복된 원소를 포함 할 수 있음
    for i in range(0, len(str1) - 1):
        if str1[i : i + 2].isalpha():
            arr1.append(str1[i : i + 2].lower())
        
    for i in range(0, len(str2) - 1):
        if str2[i : i + 2].isalpha():
            arr2.append(str2[i : i + 2].lower())
    
    # 다중집합의 교집합
    intersect = list((Counter(arr1) & Counter(arr2)).elements())
    
    # 다중집합의 합집합
    union = list((Counter(arr1) | Counter(arr2)).elements())
               
        
    if not(intersect) and not(union):
        return 65536
    
    else:
        return int((len(intersect) / len(union)) * 65536)
    
    
print(solution("FRANCE", "french")) # 16384
print(solution("handshake", "shake hands")) # 65536
print(solution("aa1+aa2", "AAAA12"))    # 43698
print(solution("E=M*C^2", "e=m*c^2"))   # 65536
