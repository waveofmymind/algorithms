def solution(s, skip, index):
    answer=""
    skip = list(map(ord,skip))
    for x in s:
        tmp = ord(x)
        cnt = 0
        while cnt < index:
            tmp += 1
            
            if tmp > ord("z"):
                tmp = ord("a")
            if tmp in skip:
                continue
            else:
                cnt += 1
        answer += chr(tmp)
    return answer
    
        
    