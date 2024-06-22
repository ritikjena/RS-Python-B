def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    transposed = [[0] * m for _ in range(n)]
    
    for i in range(m):
        for j in range(n):
            transposed[j][i] = matrix[i][j]
    
    return transposed

print(transpose([[1,2,3],[4,5,6],[7,8,9]])) 
print(transpose([[1,2,3],[4,5,6]]))         
