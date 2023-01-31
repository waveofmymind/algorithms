def solution(routes):
    cnt = 1
    routes.sort(key=lambda x:x[1])
    tmp = routes[0][1] #카메라 위치의 최대값
    print(routes)
    for i in range(1,len(routes)):
        print(tmp)
        if routes[i][0] <= tmp: 
            pass
        elif routes[i][0] > tmp:
            cnt += 1
            tmp = routes[i][1]
    return cnt
            
            