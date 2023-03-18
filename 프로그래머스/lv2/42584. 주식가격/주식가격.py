def solution(prices):
    answer = [0]*len(prices)
    stack = []
    for i in range(len(prices)):
        if not stack:
            stack.append((i,prices[i]))
        else:
            while stack and stack[-1][1] > prices[i]:
                day,v = stack.pop()
                answer[day] = i - day
        stack.append((i,prices[i]))
    
    for x,y in stack:
        answer[x] = len(prices)-x-1
    return answer