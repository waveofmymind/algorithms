from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    kg = deque(people)

    while kg:

        if len(kg) >=2:
            if kg[0] + kg[-1] <= limit:
                kg.popleft()
                kg.pop()
                answer +=1
            elif kg[0] + kg[-1] > limit:
                kg.pop()
                answer+=1
        else:
            kg.pop()
            answer +=1






    return answer