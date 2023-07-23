def rotate(matrix,rows,columns):
    for i in range(rows):
        for j in range(i,rows):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(rows):
        matrix[i]=matrix[i][::-1]

    return matrix

matrix=[]
rows=int(input("No of rows : "))
columns=int(input("No of columns : "))
for i in range(rows):
    matrix.append(list(map(int,input().split())))
print(rotate(matrix,rows,columns))