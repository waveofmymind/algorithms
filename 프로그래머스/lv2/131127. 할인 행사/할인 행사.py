from collections import Counter
def solution(want, number, discount):
    dict = {}
    answer = 0
    for i in range(len(want)):
        dict[want[i]] = number[i]
    
    for i in range(len(discount)-9):
        c1 = Counter(discount[i:i+10])
        if dict == c1:
            answer += 1
    return answer
            
        
        