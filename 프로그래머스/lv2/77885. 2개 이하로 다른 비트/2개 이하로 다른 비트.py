def solution(numbers):
    arr = []
    answer =  []
    for num in numbers:
        arr.append('0'+bin(num)[2:])
    
    for i in range(len(numbers)):
        if numbers[i]%2 == 0: #짝수이면 가장 오른쪽 비트 1로
            answer.append(int(''.join(arr[i][:-1]+'1'),2))
        else:
            idx = arr[i].rfind('0')
            answer.append(int(''.join(arr[i][:idx]+'1'+'0'+arr[i][idx+2:]),2))
    return answer  
            