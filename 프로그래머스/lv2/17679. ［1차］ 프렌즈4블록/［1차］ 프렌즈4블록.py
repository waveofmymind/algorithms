def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    s = set()
    cnt = 0
    while True:
        for y in range(m-1):
            for x in range(n-1):
                tmp = board[y][x]
                if tmp == []:
                    continue
                if tmp == board[y+1][x] and tmp == board[y+1][x+1] and tmp == board[y][x+1]:
                        s.add((x,y))
                        s.add((x+1,y))
                        s.add((x,y+1))
                        s.add((x+1,y+1))
        if s:
            cnt += len(s)
            for x,y in s:
                board[y][x] = []
            s = set()
        else:
            return cnt 
        
        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j]==[]:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved == 0:
                break 
            
        