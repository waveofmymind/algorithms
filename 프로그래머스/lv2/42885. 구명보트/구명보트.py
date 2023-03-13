from collections import deque

def solution(people, limit):
    cnt = 0
    people.sort()
    q = deque(people)
    
    while q:
        if len(q) >= 2:
            if q[0] + q[-1] <= limit:
                cnt += 1
                q.pop()
                q.popleft()
            else:
                q.pop()
                cnt += 1
        else:
            q.pop()
            cnt += 1
            break
    return cnt
                