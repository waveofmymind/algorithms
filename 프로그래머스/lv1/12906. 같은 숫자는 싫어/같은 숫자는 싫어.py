def solution(arr):
    stack = []
    for a in arr:
        while stack and stack[-1] == a:
            stack.pop()
        stack.append(a)
    return stack