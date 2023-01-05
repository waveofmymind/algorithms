n, m = map(int,input().split())
arr = list(map(int,input().split()))
selected = []
arr.sort()
def dfs(start):
    if len(selected) == m:
        return print(' '.join(map(str,selected)))
    for i in arr:
        if len(selected) != 0:
            if selected[-1] <= i:
                selected.append(i)
                dfs(i)
                selected.pop()
        else:
            selected.append(i)
            dfs(i)
            selected.pop()

dfs(1)

