n = int(input())

maxArr = [0]*3
minArr = [0]*3

maxBuf = [0]*3
minBuf = [0]*3

for i in range(n):
    a,b,c= map(int,input().split())
    for i in range(3):
        if i == 0:
            maxArr[i] = a + max(maxBuf[i],maxBuf[i+1])
            minArr[i] = a + min(minBuf[i],minBuf[i+1])
        elif i == 1:
            maxArr[i] = b + max(maxBuf[i-1],maxBuf[i],maxBuf[i+1])
            minArr[i] = b + min(minBuf[i-1],minBuf[i],minBuf[i+1])
        else:
            maxArr[i] = c + max(maxBuf[i-1], maxBuf[i])
            minArr[i] = c + min(minBuf[i-1], minBuf[i])
    for i in range(3):
        maxBuf[i] = maxArr[i]
        minBuf[i] = minArr[i]
print(max(maxArr),min(minArr))


