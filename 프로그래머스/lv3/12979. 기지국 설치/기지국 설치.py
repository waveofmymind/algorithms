from math import ceil
def solution(n, stations, w):
    answer = 0
    dist = 2*w+1
    st = 1
    for i in stations:
        tmp = i-w-st
        if tmp > 0:
            answer += ceil(tmp/dist)
        st = i+w+1
        
    if n >= st:
        answer += ceil((n-st+1)/dist)
    return answer