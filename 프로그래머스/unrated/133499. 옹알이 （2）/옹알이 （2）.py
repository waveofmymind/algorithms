def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for b in babbling:
        for w in word:
            if w*2 not in b:
                b=b.replace(w,' ')
        if len(b.strip()) == 0:
            cnt +=1
    return cnt
    
    
            