from collections import Counter

def solution(topping):
    cnt = 0
    c = Counter(topping)
    s = set()
    for i in topping:
        c[i] -= 1
        s.add(i)
        if c[i] == 0:
            c.pop(i)
        if len(c) == len(s):
            cnt += 1
    return cnt
    
        
        
        