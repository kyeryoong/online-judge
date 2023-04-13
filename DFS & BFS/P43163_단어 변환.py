# P43163. 게임 맵 최단거리
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/43163


from collections import deque


# 두 단어가 한 글자만 차이 나는지 확인하는 함수
def wordDiff(word1, word2):
    diff = 0
    word1 = list(word1)
    word2 = list(word2)

    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            diff = diff + 1

    return diff == 1


def solution(begin, target, words):
    # 큐에 (단어, 단계) 형식으로 삽입
    queue = deque([(begin, 0)])

    # 방문한적이 있는 단어
    visited = []

    # 너비 우선 탐색 알고리즘
    while queue:
        current_word, current_count = queue.popleft()

        # 현재 단어가 target과 일치하면 현재 단계를 반환
        if current_word == target:
            return current_count

        for word in words:
            # wordDiff(current_word, word): 현재 단어와 한 글자만 차이 나는 단어로만 이동
            # word not in visited: 방문한적이 없는 단어로만 이동
            if wordDiff(current_word, word) and word not in visited:
                queue.append((word, current_count + 1))
                visited.append(word)

    # 변환할 수 없는 경우 0을 반환
    return 0


print(solution("hit", "cog", ))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))   # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]))  # 1
print(solution("1234567000", "1234567899", [
      "1234567800", "1234567890", "1234567899"]))  # 3
print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]))  # 4
