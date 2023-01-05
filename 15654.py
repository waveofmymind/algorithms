n, m = map(int,input().split())
arr = list(map(int,input().split()))
selected = []
arr.sort()
def dfs(start):
    if len(selected) == m:
        return print(' '.join(map(str,selected)))
    for i in arr:
        if i not in selected:
            selected.append(i)
            dfs(i+1)
            selected.pop()

dfs(1)

