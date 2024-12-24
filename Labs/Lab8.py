def countPaths(n: int, m: int) -> int:
    # Your code here

    
    grid =[[0 for _ in range(m+1)] for _ in range(n+1)]

    # Base conditions: Fill first row and columns with 1
    for i in range(n+1):
        grid[i][0] = 1
    
    for j in range(m+1):
        grid[0][j] = 1
    

    # print(grid)


    for i in range(1,n+1):
        for j in range(1,m+1):
            grid[i][j] = grid[i][j-1] + grid[i-1][j]

    
    return(grid[n][m])    

# countPaths(2,2)