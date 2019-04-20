def find_mountain(matrix):
    res_i, res_j, maxx = 0, 0, 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if maxx < matrix[i][j]:
                res_i, res_j = i, j
                maxx = matrix[i][j]
    return (res_i, res_j)
                