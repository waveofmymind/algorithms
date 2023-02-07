from itertools import combinations,permutations
from collections import deque
def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))
    
def calculate(exp,op):
    buf = ""
    arr = []
    for i in exp:
        if i.isdigit()==True:
            buf += i
        else:
            arr.append(buf)
            arr.append(i)
            buf = ""
    arr.append(buf)
    
    for o in op:
        stack = []
        while len(arr) != 0:
            tmp = arr.pop(0)
            if tmp == o:
                stack.append(operation(stack.pop(),arr.pop(0),o))
            else:
                stack.append(tmp)
        arr = stack
    return abs(int(arr[0]))
        

def solution(expression):
    c = ['*','-','+']
    result = []
    check = list(permutations(c,3))
    for op in check:
        result.append(calculate(expression,op))
    return max(result)