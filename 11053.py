from collections import deque

n = int(input())
arr = deque(map(int,input().split()))

dp = [0] * n

for i in range(n): # n개까지의 최소 문자열 개수, ex i = 3일때 값 30
    for j in range(i): # j = 0,1,2
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))

