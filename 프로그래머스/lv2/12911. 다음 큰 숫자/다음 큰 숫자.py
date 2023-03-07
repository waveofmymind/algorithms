def solution(n):
    change_n = bin(n)[2:]
    tmp = n
    while True:
        tmp += 1
        change_tmp = bin(tmp)[2:]
        if change_n.count('1') == change_tmp.count('1'):
            return tmp
            