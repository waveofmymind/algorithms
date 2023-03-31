from collections import deque
def solution(s):
    answer = 0
    arr = deque(s)
    cnt = 0
    
    for _ in range(len(s)):
        arr.append(arr.popleft())
        if check(arr):
            cnt += 1
    return cnt

def check(change_list):
        stack = []
        for i in change_list:
            if not stack:
                stack.append(i)
            else:
                if i == '}' and stack[-1] == '{':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        
        return True if len(stack)==0 else False
    
