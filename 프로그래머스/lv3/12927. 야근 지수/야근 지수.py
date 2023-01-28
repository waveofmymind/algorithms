from collections import deque
import heapq
def solution(n, works):
    if n >= sum(works):
        return 0
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        tmp = heapq.heappop(works)
        tmp += 1
        heapq.heappush(works, tmp)
        
    return sum([w ** 2 for w in works])
    
            
        