def solution(k, m, score):
    score.sort(reverse=True)
    s = len(score)%m
    answer = 0
    for i in range(0,len(score)-m+1,m):
        answer += min(score[i:i+m])*m
    return answer
                