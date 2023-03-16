import math

def solution(arr):
    total = arr[0]
    for i in arr[1:]:
        total = total*i//math.gcd(total,i)
    return total
        