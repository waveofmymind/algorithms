def solution(n):
    cnt = 0
    while n != 0:
        cnt += n%2
        n //= 2
    return cnt
        
        
            