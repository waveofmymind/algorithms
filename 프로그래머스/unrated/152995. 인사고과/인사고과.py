def solution(scores):
    target = scores[0]
    target_sum = sum(target)
    scores.sort(key=lambda s: (-s[0], s[1]))
    max_company, answer = 0, 1
    for s in scores:
        if target[0] < s[0] and target[1] < s[1]:
            return -1
        if max_company <= s[1]:
            if target_sum < s[0] + s[1]:
                answer += 1
            max_company = s[1]
    return answer

    
            
             
        
        