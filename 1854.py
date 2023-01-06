import heapq
import sys
input = sys.stdin.readline
INF = 9876543210
n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

distance = [[INF] * (k) for _ in range(n+1)]


q = []
heapq.heappush(q,(0,1))

distance[1][0] = 0


while q:
    dist,now = heapq.heappop(q)
    for next,next_dist in graph[now]:
        if distance[next][k-1] > dist + next_dist:
            distance[next][k-1] = dist + next_dist
            distance[next] = sorted(distance[next])
            heapq.heappush(q,(dist+next_dist,next))
print(distance)
for _ in range(1,n+1):
    print(-1 if distance[_][k-1] == INF else distance[_][k-1])