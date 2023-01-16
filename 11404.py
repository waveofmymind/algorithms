import sys
INF = 9876543210
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph= [[INF] *n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    if graph[a-1][b-1] > c:
        graph[a-1][b-1] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]
for i in graph:
    for j in i:
        if j == INF:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()


