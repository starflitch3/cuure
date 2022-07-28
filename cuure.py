def maxValue(matrix, lig, col):
    
    path = []
 
    global sum
    sum = [[0 for i in range(lig + 1)] 
                for i in range(col + 1)]

   
    for i in range(1, col + 1):
        for j in range(1, lig + 1):
 
            sum[i][j] = (max(sum[i - 1][j], sum[i][j - 1]) + matrix[i - 1][j - 1])

    Y = col
    X = lig

    for k in range(Y,0, -1):
        for l in range(X,0, -1):
            if sum[k-1][l] >= sum[k][l-1]:
                path.append([k-1,l-1])
                Y -= 1
                break
            elif sum[k-1][l] < sum[k][l-1]:
                path.append([k-1,l-1])
                X -= 1
    print(path[::-1])

    return sum[col][lig]
 


matrix = [
[1,3,5,2],
[2,0,3,1],
[4,2,1,2],
[1,0,2,1]]

N = len(matrix)
M = len(matrix[0])
 
max_matrix = maxValue(matrix, M, N)
print( max_matrix)

