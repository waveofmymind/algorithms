import heapq
import sys
INF = 9876543210
v,e = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))

distance = [INF] *(v+1)
distance[start] = 0
q = []
heapq.heappush(q,(0,start))
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for next,next_dist in graph[now]:
        cost = dist+next_dist
        if cost < distance[next]:
            distance[next] = cost
            heapq.heappush(q,(cost,next))


for i in range(1,len(distance)):
    if distance[i] == 9876543210:
        print("INF")
    else:
        print(distance[i])



