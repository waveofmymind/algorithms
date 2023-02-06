from collections import deque
def sep(p):
    open_s,close_s = 0,0
    for i in range(len(p)):
        if p[i] == '(':
            open_s += 1
        if p[i] == ')':
            close_s += 1
        if open_s == close_s:
            u = p[:i+1]
            v = p[i+1:]
            return u,v
        
def check(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True if not stack else False


def solution(p):
    if not p:
        return p
    u,v = sep(p)
    if check(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        for x in u[1:len(u)-1]:
            if x == '(':
                answer += ')'
            else:
                answer += '('
    return answer  