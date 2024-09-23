import numpy as np
def can_solve(y,x,n,grid):
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
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for k in range(1,10):
                    if can_solve(i,j,k,grid) == True:
                        grid[i][j] = k
                        solve(grid) 
                        grid[i][j] = 0
                return
    print(np.matrix(grid))