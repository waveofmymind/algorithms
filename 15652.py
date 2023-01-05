n, m = map(int,input().split())
# m개 선택, 중복 가능, 오름차순
selected = []
def dfs(start):
    if len(selected) == m:
        return print(' '.join(map(str,selected)))
    for i in range(1,n+1):
        if len(selected) != 0:
            if selected[-1] <= i:
                selected.append(i)
                dfs(i+1)
                selected.pop()
        else:
            selected.append(i)
            dfs(i+1)
            selected.pop()
dfs(1)



