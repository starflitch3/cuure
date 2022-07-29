def maxValue(matrix, lig, col):
    
    path = []
 
    global sum
    #créer une deuxième matrice remplie de zero
    sum = [[0 for i in range(lig + 1)] 
                for i in range(col + 1)]

   
    for i in range(1, col + 1):
        for j in range(1, lig + 1):
            #à chaque fois je prend la somme du nombre en haut à droite de la case que je veux remplire
            #dans la matrice de base et je l'additionne avec le nombre le plus grand en haut ou à gauche
            #dans la nouvelle matrice que j'ai crée. Cela m'assure de prendre le chemin avec la plus grosse
            #somme à chaque fois
            sum[i][j] = (max(sum[i - 1][j], sum[i][j - 1]) + matrix[i - 1][j - 1])

    Y = col
    X = lig
    #pour récuperer le chemin, je remonte la matrice remplie avec les sommes et je prend le plus grand 
    # en haut ou a gauche
    for k in range(Y,0, -1):
        for l in range(X,0, -1):
            if sum[k-1][l] >= sum[k][l-1]:
                path.append([k-1,l-1])
                Y -= 1
                break
            elif sum[k-1][l] < sum[k][l-1]:
                path.append([k-1,l-1])
                X -= 1
    #inverse le path car il est à l'envers
    print(path[::-1])

    return sum[col][lig]
 


matrix = [
[1,3,5,2],
[2,0,3,1],
[4,2,1,2],
[1,0,2,1]]

col = len(matrix)
lig = len(matrix[0])
 
max_matrix = maxValue(matrix, lig, col)
print( max_matrix)

