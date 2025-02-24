# User input
matrix=input("Enter the matrix: ")

# Function to transpose a matrix
def matrix_transpose(mat):
    M=[] # Initialize an empty list to store the transposed matrix
    for i in range(len(mat)):
        temp=[]  # Temporary list to store each row of the transposed matrix
        for j in range(len(mat[0])):
            temp.append(mat[j][i])
        M.append(temp)
    return M
print("Transpose of the matrix is: ",matrix_transpose(matrix))
