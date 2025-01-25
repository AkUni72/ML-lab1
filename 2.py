def create_matrix(m,n):
    matrix=[]
    for i in range(m):
        temp=[]
        for j in range(n):
            element=eval(input("Enter the element: "))
            temp.append(element)
        matrix.append(temp)
    return matrix

def check_multiplicity(a,b):
    a_col=len(a[0])
    b_row=len(b)
    if a_col==b_row:
        return True
    else:
        return False

def mutiply_matrices(a,b):
    matrix = []

    for i in range(len(A)):
        mat = []
        temp = []
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(B)):
                sum += (A[i][k]) * (B[k][j])
            temp.append(sum)
        mat.append(temp)
        matrix.append(temp)
    return matrix

A=create_matrix(2,3)
B=create_matrix(3,2)
if check_multiplicity(A,B)==True:
    print("The matrices can be multiplied")
else:
    print("The matrices cannot be multiplied")
C=mutiply_matrices(A,B)
print(C)