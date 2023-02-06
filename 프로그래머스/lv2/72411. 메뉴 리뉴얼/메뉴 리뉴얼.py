from itertools import product,combinations,permutations
from collections import Counter
def solution(orders, course):
    arr = []

    answer = []
    for i in course:
        result = []
        for order in orders:
            combi = combinations(sorted(order),i)
            result += combi
          
        c1 = Counter(result)
        if len(c1) != 0 and max(c1.values()) != 1:
            answer += [''.join(f) for f in c1 if c1[f] == max(c1.values())]
    return sorted(answer)
                
    