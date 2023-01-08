
n,m = map(int,input().split())
arr = sorted(list(set(map(int,input().split()))))
sel =[]
visited = [0] * 10
ans = []

def dfs(depth):
    if depth == m:
        print(" ".join(map(str,sel)))
        return
    for i in arr:
        if depth == 0 or sel[-1] <= i:
            sel.append(i)
            dfs(depth+1)
            sel.pop()

dfs(0)





