# Function to create a matrix 
def create_matrix(m, n):
    matrix = []
    for i in range(m):  # Loop through rows
        temp = []
        for j in range(n):  # Loop through columns
            element = eval(input("Enter the element: "))  
            temp.append(element)  # Add element to row
        matrix.append(temp)  # Add row to matrix
    return matrix

# Function to check if two matrices can be multiplied
def check_multiplicity(a, b):
    a_col = len(a[0])  # Number of columns in matrix A
    b_row = len(b)  # Number of rows in matrix B
    return a_col == b_row  # Return True if multiplication is possible

# Function to multiply matrices
def multiply_matrices(A, B):  
    matrix = []  # Initialize result matrix
    for i in range(len(A)):  # Loop over rows of A
        temp = []
        for j in range(len(B[0])):  # Loop over columns of B
            sum_value = 0  # Initialize sum for dot product
            for k in range(len(B)):  # Loop over rows of B 
                sum_value += A[i][k] * B[k][j]  # Compute dot product
            temp.append(sum_value)  # Append computed value to row
        matrix.append(temp)  # Append row to result matrix

    return matrix  # Return resultant matrix

# Creating matrices with user input
A = create_matrix(2, 3)  # Create first matrix of size 2x3
B = create_matrix(3, 2)  # Create second matrix of size 3x2

# Check if multiplication is possible
if check_multiplicity(A, B):
    print("The matrices can be multiplied")
    C = multiply_matrices(A, B)  # Perform matrix multiplication
    print("Resultant Matrix:", C)
else:
    print("The matrices cannot be multiplied")
