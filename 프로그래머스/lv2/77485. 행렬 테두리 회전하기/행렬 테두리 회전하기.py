def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for i in range(columns+1)] for j in range(rows+1)]
    num = 1
    for row in range(1, rows+1):
        for column in range(1, columns+1):
            matrix[row][column] = num
            num += 1
    
    for x1,y1,x2,y2 in queries:
        saved = matrix[x1][y1]
        buf = saved
        
        for i in range(x1,x2):
            tmp = matrix[i+1][y1]
            matrix[i][y1] = tmp
            buf = min(buf,tmp)
            
        for i in range(y1,y2):
            tmp = matrix[x2][i+1]
            matrix[x2][i] = tmp
            buf = min(buf,tmp)
            
        for i in range(x2,x1,-1):
            tmp = matrix[i-1][y2]
            matrix[i][y2] = tmp
            buf = min(buf,tmp)
    
        for i in range(y2,y1,-1):
            tmp = matrix[x1][i-1]
            matrix[x1][i] = tmp
            buf = min(buf,tmp)
            
        matrix[x1][y1+1] = saved
        answer.append(buf)
    return answer