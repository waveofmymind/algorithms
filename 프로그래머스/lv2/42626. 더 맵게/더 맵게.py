import heapq as hq
def solution(scoville, K):
    hq.heapify(scoville)
    mix_cnt = 0
    while len(scoville)>=2:
        a = len(scoville)
        target1 = hq.heappop(scoville)
        if target1 >= K:
            break
        target2 = hq.heappop(scoville)
        hq.heappush(scoville,target1+target2*2)
        mix_cnt += 1
        if len(scoville) < 2 and scoville[0] < K:
            return - 1
    return mix_cnt
    
        
        
            
            
        
        