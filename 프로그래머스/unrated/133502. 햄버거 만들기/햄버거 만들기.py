def solution(ingredient):
    make = [1,2,3,1]
    cnt = 0
    s = []
    for i in ingredient:
        s.append(i)
        if s[-4:] == make:
            cnt += 1
            for _ in range(4):
                s.pop()
    return cnt
            
            