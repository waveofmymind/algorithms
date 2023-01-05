import sys

n, m, b = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
board = [0] * 257
cnt = 1e9
result = 0
ans = int(1e9)

for x in range(257): # 내가 고르게 할 땅의 블록 수
    maxValue,minValue = 0,0
    for i in range(n):
        for j in range(m):
            if ground[i][j] > x: #고르게 할 땅의 블록 수보다 블록이 높을 경우 블록을 x까지 빼서 인벤토리에 넣어야한다.(남는 블록 수)
                maxValue += ground[i][j] - x
            else: #고르게 할 땅의 블록 수보다 블록이 낮을 경우 (필요한 블록 수)
                minValue += x-ground[i][j]

    if maxValue + b < minValue: #남는 블록이 필요한 블록 수보다 많아야 땅을 고르게 할 수 있다.
        continue
    cnt = maxValue*2+minValue
    if cnt <= ans:
        ans = cnt
        result = x

print(ans, result)






