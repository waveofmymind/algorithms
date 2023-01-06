import heapq
from collections import deque
from heapq import heappush, heappop
import sys
INF = 9876543210
m,n = map(int,input().split())
miro = [list(map(int,input())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]

q = deque()
q.append((0,0))
distance = [[-1]*m for _ in range(n)]
distance[0][0] = 0
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=ny<n and 0<=nx<m :
            if distance[ny][nx] == -1:
                if miro[ny][nx] == 0:
                    distance[ny][nx] = distance[y][x] #가중치가 0이므로, 계속 탐색해본다.
                    q.appendleft((nx,ny))
                else:
                    distance[ny][nx] = distance[y][x] + 1
                    q.append((nx,ny))

print(distance[n-1][m-1])









