# 17626.Four Squares
import math

n = int(input())

if math.sqrt(n).is_integer():
    print(1) # n의 제곱근이 정수일 경우 1
    exit(0)
for i in range(1,int(math.sqrt(n))+1):
    if math.sqrt((n-i**2)).is_integer():
        print(2) # 1부터 n의 제곱근을 정수화 한 값을 i라고 하면 n에서 i의 제곱을 뺀 값이 정수이면 2
        exit(0)
for i in range(1, int(n**0.5)+1) :
        for j in range(1, int((n-i*i)**0.5)+1) :
            if ((n-i*i-j*j)**0.5).is_integer() :
                print(3)
                exit(0)
print(4)

