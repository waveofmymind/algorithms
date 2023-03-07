def solution(n):
    count_n = bin(n)[2:].count('1')
    tmp = n
    while True:
        tmp += 1
        if bin(tmp)[2:].count('1') == count_n:
            return tmp
            