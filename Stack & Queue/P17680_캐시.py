# P17680. 캐시
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/17680


def solution(cacheSize, cities):
    cache = []

    # 캐시 크기가 0이면 항상 cache miss가 일어남
    if cacheSize == 0:
        return 5 * len(cities)

    # 총 실행시간
    answer = 0


    for i in range(0, len(cities)):
        
        # 입력된 도시이름이 캐시에 있는 경우
        if cities[i].lower() in cache:
            
            # 해당 도시이름을 캐시에서 삭제
            cache.remove(cities[i].lower())
            
            # 해당 도시이름을 다시 캐시 맨 뒤에 삽입
            cache.append(cities[i].lower())

            # 실행시간 1초 증가
            answer = answer + 1


        # 입력된 도시이름이 캐시에 없는 경우
        else:
            
            # 캐시가 꽉찬 경우
            if len(cache) == cacheSize:
                
                # 캐시 가장 앞에 있는 도시이름을 삭제
                cache.pop(0)

            # 새로운 도시이름을 캐시 맨 뒤에 삽입
            cache.append(cities[i].lower())

            # 실행시간 5초 증가
            answer = answer + 5
            

    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))    # 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))   # 21
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))   # 60
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))   # 52
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))    # 16
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))    # 25
