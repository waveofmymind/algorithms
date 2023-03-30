def solution(operations):
    com,num = [],[]
    arr = []
    for op in operations:
        com,num= op.split(" ")
        if com == 'I': #값을 큐에 넣고
            arr.append(int(num))
            arr.sort() #오름차순 정렬
        else:
            if arr:
                if num == '-1':
                    arr.pop(0) #최솟값 빼기
                else:
                    arr.pop() #최댓값 빼기
            else:
                continue 

    if arr:
        return [max(arr),min(arr)]
    else:
        return [0,0]