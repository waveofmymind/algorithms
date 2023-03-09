def solution(s):
    stack = []
    for s in s:
        if not stack:
            stack.append(s)
        else:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
    if stack:
        return 0
    else:
        return 1
        