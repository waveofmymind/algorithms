import heapq
from heapq import heappush, heappop
import sys

INF = 98765432109876543210
n,m,k = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance = [[INF] * (k+1) for _ in range(n+1)]
q = []
for i in range(k+1):
    distance[1][i] = 0
heapq.heappush(q, (0, 1, 0))

while q:
    dist, now, p = heapq.heappop(q)
    if distance[now][p] < dist:
        continue
    if p+1 <= k:
        for (idx, x) in graph[now]:
            if distance[idx][p+1] > dist:
                distance[idx][p+1] = dist
                heapq.heappush(q, (dist, idx, p+1))

    for (idx, x) in graph[now]:
        cost = x + dist
        if distance[idx][p] > cost:
            distance[idx][p] = cost
            heappush(q,(cost,idx,p))

ans = INF
for i in range(k+1):
    ans = min(ans, distance[n][i])
print(ans)




