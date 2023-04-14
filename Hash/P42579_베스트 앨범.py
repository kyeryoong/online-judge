# P42579. 베스트 앨범
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/42579


def solution(genres, plays):
    # 노래 재생 횟수를 장르별로 분류
    plays_by_genre = {}

    # 장르별 총 재생 횟수
    genre_total_plays = {}

    for genre in genres:
        if genre not in plays_by_genre:
            plays_by_genre[genre] = []

        if genre not in genre_total_plays:
            genre_total_plays[genre] = 0

    for i in range(0, len(plays)):
        # 모든 노래를 장르별로 분류하고 (고유 번호, 재생 횟수) 형식으로 저장
        plays_by_genre[genres[i]].append((i, plays[i]))

        # 해당 장르의 총 재생 횟수에 추가
        genre_total_plays[genres[i]] = genre_total_plays[genres[i]] + plays[i]


    # 장르별 재생 횟수로 정렬
    genre_ranking = list(genre_total_plays.items())
    genre_ranking.sort(key=lambda x: x[1], reverse=True)
    
    # 장르만 추출
    genre_ranking = [i[0] for i in genre_ranking]


    # 베스트 앨범에 들어갈 노래의 고유 번호
    answer = []

    for genre in genre_ranking:
        # x[1]: 장르 내에서 많이 재생된 노래를 먼저 정렬
        # -x[0]: 장르 내에서 재생 횟수가 같은 노래 중에서 고유 번호가 낮은 노래를 먼저 정렬        
        plays_by_genre[genre].sort(key=lambda x: (x[1], -x[0]), reverse=True)
        plays_by_genre[genre] = [i[0] for i in plays_by_genre[genre]]

        # 각 장르 별로 가장 많이 재생된 노래를 두 개씩 베스트 앨범에 추가
        answer = answer + plays_by_genre[genre][0: 2]


    return answer
