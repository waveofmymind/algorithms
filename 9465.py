import sys
from collections import deque

input = sys.stdin.readline
INF = 1e9
dx = [0,0,1,-1]
dy = [-1,1,0,0]
t = int(input())


for _ in range(t):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(2)]
    visited = [[False] * n for _ in range(2)]
    total = 0

    for j in range(1,n):
        if j == 1:
            arr[0][j] += arr[1][j-1]
            arr[1][j] += arr[0][j-1]
        else:
            arr[0][j] += max(arr[1][j-1], arr[1][j-2])
            arr[1][j] += max(arr[0][j - 1], arr[0][j - 2])
    print(max(arr[0][n-1],arr[1][n-1]))




