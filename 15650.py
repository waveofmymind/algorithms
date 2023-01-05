from collections import deque

n, m = map(int,input().split())
arr = [i for i in range(1,n+1)]

selected = []
def dfs(start):
    if len(selected) == m:
        print(' '.join(map(str,selected)))
        return
    for i in range(start,n+1):
        if i not in selected:
            selected.append(i)
            dfs(i+1)
            selected.pop()
dfs(1)





