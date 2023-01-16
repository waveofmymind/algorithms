import sys

input = sys.stdin.readline
n = int(input())

arr = [0] * n
ans = 0
def check(x):
    for i in range(x):
        if arr[i] == arr[x] or abs(x-i) == abs(arr[i]-arr[x]):
            return False
    return True

def main(depth):
    global ans
    if depth == n:
        ans += 1

    else:
        for i in range(n):
            arr[depth] = i
            if check(depth):
                main(depth+1)
main(0)
print(ans)