from collections import deque
def solution(people, limit):
    cnt = 0
    people.sort()
    lt = 0
    rt = len(people)-1
    while lt<=rt:
        cnt += 1
        if (people[lt] + people[rt] <= limit):
            lt += 1
            rt -= 1
        else:
            rt -= 1
    return cnt
    
    
        
        
            
            
            
        