
def solution(n,a,b):
    cnt = 1
    while True:
        if (b%2 == 0 and a + 1 == b) or ((a%2==0) and b + 1 == a):
            return cnt
        a = (a + 1) //2
        b = (b+1) //2
        cnt += 1
    

    