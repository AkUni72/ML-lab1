matrix=input("Enter the matrix: ")
def matrix_transpose(mat):
    M=[]
    for i in range(len(mat)):
        temp=[]
        for j in range(len(mat[0])):
            temp.append(mat[j][i])
        M.append(temp)
    return M
print("Transpose of the matrix is: ",matrix_transpose(matrix))