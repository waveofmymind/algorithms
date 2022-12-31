#11403. 경로 찾기


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]



for k in range(n): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 or (arr[i][k] == 1 and arr[k][j] == 1):
                arr[i][j] = 1

for x in arr:
    for y in x:
        print(y, end=' ')
    print()