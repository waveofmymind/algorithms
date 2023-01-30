def solution(files):
    arr =  []
    head,number,tail = '','',''
    for file in files:
        for i in range(len(file)):
            if file[i].isdigit(): #숫자이면 그 전까지 헤드
                head = file[:i]
                number = file[i:] #number+tail
                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                arr.append([head,number,tail])
                head,number,tail = '','',''
                break
    arr.sort(key=lambda x:(x[0].lower(),int(x[1])))
    return [''.join(i) for i in arr]