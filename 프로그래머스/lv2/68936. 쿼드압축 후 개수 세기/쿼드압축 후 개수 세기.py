def solution(arr):
    answer = [0,0]
    n = len(arr)
    def dfs(x,y,n):
        st = arr[x][y]
        for i in range(x,x+n):
            for j in range(y,y+n):
                if arr[i][j] != st:
                    nn = n//2
                    dfs(x,y,nn)
                    dfs(x+nn,y,nn)
                    dfs(x,y+nn,nn)
                    dfs(x+nn,y+nn,nn)
                    return
        answer[st] += 1
    dfs(0,0,n)
    return answer
    