from collections import deque

def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return false
            else:
                stack.append(i)
    if not stack:
        return True
    else:
        return False
                    
                    
        