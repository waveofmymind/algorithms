import sys


arr1 = sys.stdin.readline().rstrip()
arr2 = sys.stdin.readline().rstrip()
len1 = len(arr1)
len2 = len(arr2)

matrix = [[0]*(len2+1) for _ in range(len1+1)]

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if arr1[i-1] == arr2[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])

print(matrix[-1][-1])