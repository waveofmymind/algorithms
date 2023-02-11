import heapq
def solution(k, score):
    rank = []
    answer = []
    for x in score:
        if len(rank) == k:
            heapq.heappush(rank,x)
            heapq.heappop(rank)
         
        else:
            heapq.heappush(rank,x)
        answer.append(rank[0])
    return answer
            
                