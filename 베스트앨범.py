import heapq
def solution(genres, plays):
    answer = []
    genre_cnt = dict()
    plays_cnt = dict()
    for idx, genre in enumerate(genres):
        if genre_cnt.get(genre): 
            genre_cnt[genre] += plays[idx]
            heapq.heappush(plays_cnt[genre], (-plays[idx], idx))
        else: 
            genre_cnt[genre] = plays[idx]
            plays_cnt[genre] = []
            heapq.heappush(plays_cnt[genre], (-plays[idx], idx))
    
    new_list = sorted(genre_cnt.items(), key = lambda x : x[1])
    while new_list:
        genre, cnt = new_list.pop()
        for _ in range(2):
            if plays_cnt[genre]:
                cnt, idx = heapq.heappop(plays_cnt[genre])
                answer.append(idx)

    return answer
