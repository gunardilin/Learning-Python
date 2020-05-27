import datetime
n = 5
 
def isSafe(nextX, nextY, board):
    if 0<=nextX<n and 0<=nextY<n:
        if board[nextX][nextY] == -1:
            return True 
    return False 

def printSolution(n, board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end="\t")
        print()

def solveKT(n):
    board = [[-1 for i in range(n)]for i in range(n)]
    startX = 0
    startY = 0
    step = 0
    board[startX][startY] = step
    moveX = [2, 1, -1, -2, -2, -1, 1, 2]
    moveY = [1, 2, 2, 1, -1, -2, -2, -1]
    if not solveKTUtil(n, board, moveX, moveY, startX, startY, step):
        print("Solution does not exist") 
    else:
        return printSolution(n, board)
         
def solveKTUtil(n, board, moveX, moveY, currX, currY, step):
    if step + 1 == n**2:
        return True 
    for i in range(8):
        nextX = currX + moveX[i]
        nextY = currY + moveY[i]
        if isSafe(nextX, nextY, board):
            currX = nextX
            currY = nextY
            step += 1
            board[currX][currY] =  step 
            if solveKTUtil(n, board, moveX, moveY, currX, currY, step):
                return True 
            board[currX][currY] = -1
            currX -= moveX[i]
            currY -= moveY[i]
            step -= 1
    return False 
     
if __name__ == "__main__":
    startTime = datetime.datetime.now()
    solveKT(n)
    endTime = datetime.datetime.now()
    duration = endTime - startTime
    print(duration.total_seconds())
