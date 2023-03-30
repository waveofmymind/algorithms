
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
def solution(operations):
    com,num = [],[]
    q = []
    for i in operations:
        a,b= i.split(" ")
        if a == 'I':
            q.append(int(b))
            q.sort()
        else:
            if q:
                if b == '-1':
                    q.pop(0)
                else:
                    q.pop()
            else:
                continue

    if q:
        return [max(q),min(q)]
    else:
        return [0,0]