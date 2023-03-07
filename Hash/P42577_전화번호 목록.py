# P42577. 전화번호 목록
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/42577


# 풀이 1. 이중 반복문 (효율성 테스트 통과 X)
def solution1(phone_book):
    # 전화번호 두 개씩 서로 비교
    for i in range(0, len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i].startswith(phone_book[j]):
                return False
            
            if phone_book[j].startswith(phone_book[i]):
                return False
            
    return True


# 풀이 2. 단일 반복문
def solution2(phone_book):
    # 전화번호를 정렬
    phone_book.sort()
    
    # 인접한 전화번호끼리 비교
    for i in range(0, len(phone_book) - 1):
        if phone_book[i].startswith(phone_book[i + 1]):
            return False
    
    return True


# 풀이 3. 해시
def solution3(phone_book):
    # HashMap 생성
    hash_map = {}
    
    # 전화번호를 모두 HashMap에 추가
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    # 각 전화번호의 접두사가 HashMap에 존재하는지 확인
    for phone_number in phone_book:
        prefix = ""
        
        for p in phone_number:
            prefix = prefix + p
            
            # 존재하면 False 반환
            if prefix in hash_map and prefix != phone_number:
                return False
    
    return True
        

print(solution3(["119", "97674223", "1195524421"])) # False
print(solution3(["123","456","789"])) # True
print(solution3(["12","123","1235","567","88"])) # False