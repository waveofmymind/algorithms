import heapq
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
INF = 9876543210
for _ in range(m):
    a,b,c= map(int,input().split())
    graph[a].append((b,c))

start,end = map(int,input().split())
distance = [INF] * (n+1)

def djik(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for next, next_dist in graph[now]:
            cost = next_dist + dist

            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q,(cost,next))
    return distance

answer = djik(start)
print(answer[end])

