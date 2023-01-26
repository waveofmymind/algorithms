from collections import deque
def solution(skill, skill_trees):
    cnt = 0
    for skill_tree in skill_trees:
        q = deque(skill)
        for i in skill_tree:
            if not q: #큐가 비었으면 스킬트리 O
                cnt += 1
                break
            if i == q[0]:
                q.popleft()
        else:
            for j in q:
                if j in skill_tree:
                    break
            else:
                cnt += 1
    return cnt

                
        
            