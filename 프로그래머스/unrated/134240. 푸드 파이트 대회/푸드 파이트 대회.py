def solution(food):
    lt,rt = "",""
    answer = ""
    for i in range(len(food)):
        lt += str(i) * (food[i]//2)
        rt += str((len(food)-i-1))*(food[len(food)-i-1]//2)
    answer = lt+'0'+rt
    return answer