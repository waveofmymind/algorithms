def solution(s):
    answer = 0

    while s:
        target = s[0]
        target_cnt = 0
        other_cnt = 0
        for i in range(len(s)): 
            if s[i] == target:
                target_cnt += 1
            else:
                other_cnt += 1
            
            if target_cnt == other_cnt:
                s = s[i+1:]
                answer += 1
                break
        
        else:
            answer += 1
            break
    return answer
                
        