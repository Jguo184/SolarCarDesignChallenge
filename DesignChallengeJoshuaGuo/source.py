import numpy as np
sudokugrid = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
#print(np.matrix(sudoku))
def can_solve(y,x,n,grid):
    #global sudoku
    for i in range(9):
        if grid[y][i] == n:
            return False
    for j in range(9): #each row is 9 units
        if grid[j][x] == n:
            return False
    xsquare = (x//3) * 3
    ysquare = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if grid[ysquare + i][xsquare+j] == n:
                return False
    return True

def solve(grid):
    #global sudoku#but even if I declare global, it still doesn't work for the scope...why isn't it being modifed?
    #go through every single item in the sudoku 
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for k in range(1,10):
                    if can_solve(i,j,k,grid) == True:
                        grid[i][j] = k
                        solve(grid) #explain how this works, I'm a bit confused, how can this not work and still return zeros without using recursion?
                        grid[i][j] = 0
                return
    print(np.matrix(grid))
    #ok is this some weird stuff going on with the variable access? I'm a bit confused... why isn't sudoku being modified? isn't it a global variable?
    #I try modifiying it even while declaring it as a global variable, but it still doesnt work.