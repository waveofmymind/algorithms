from itertools import combinations,product
def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    arr = []
    for i in range(1,6):
        tmp=list(product(words,repeat=i))
        for j in tmp:
            arr.append(''.join(j))
    arr.sort()
    return arr.index(word)+1
