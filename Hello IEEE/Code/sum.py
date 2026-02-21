import math

def matsum(arr1, arr2):
    if len(arr1) != len(arr2) or len(arr1[0]) != len(arr2[0]):
         return "Matrices must have same dimensions"
    rows = len(arr1)
    cols = len(arr1[0])
    
    sumResult = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(arr1[i][j] + arr2[i][j])
        sumResult.append(row)
    
    return sumResult


def matsub(arr1, arr2):

    if len(arr1) != len(arr2) or len(arr1[0]) != len(arr2[0]):
         return "Matrices must have same dimensions"
    
    rows = len(arr1)
    cols = len(arr1[0])
    
    subResult = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(arr1[i][j] - arr2[i][j])
        subResult.append(row)
    
    return subResult


def matmul(arr1, arr2):
    rows1 = len(arr1)
    cols1 = len(arr1[0])
    rows2 = len(arr2)
    cols2 = len(arr2[0])

    if cols1 != rows2:
        return "Multiplication is impossible"
    
    mulResult = []
    
    for i in range(rows1):
        row = []
        for j in range(cols2):
            sum_value = 0
            for k in range(cols1):
                sum_value += arr1[i][k] * arr2[k][j]
            row.append(sum_value)
        mulResult.append(row)
    
    return mulResult


def scalarsum(scalar, arr):
    result = []
    for row in arr:
        new_row = []
        for element in row:
            new_row.append(element + scalar)
        result.append(new_row)
    return result


def scalarsub(scalar, arr):
    result = []
    for row in arr:
        new_row = []
        for element in row:
            new_row.append(element - scalar)
        result.append(new_row)
    return result


def matnorm(arr):
    flat = [element for row in arr for element in row]
    minVal = min(flat)
    maxVal = max(flat)
    
    if maxVal == minVal:
        return "Cannot normalize the matrix"
    
    norResult = []
    for row in arr:
        new_row = []
        for x in row:
            normalized = (x - minVal) / (maxVal - minVal)
            new_row.append(normalized)
        norResult.append(new_row)
    
    return norResult



rowsA = int(input("Enter number of rows for matrix A: "))
colsA = int(input("Enter number of columns for matrix A: "))

A = []
print("Enter matrix A:")
for i in range(rowsA):
    row = list(map(float, input().split()))
    A.append(row)

rowsB = int(input("Enter number of rows for matrix B: "))
colsB = int(input("Enter number of columns for matrix B: "))

B = []
print("Enter matrix B:")
for i in range(rowsB):
    row = list(map(float, input().split()))
    B.append(row)


scalar = float(input("Enter scalar value: "))




print("Sum:", matsum(A, B))
print("Subtraction:", matsub(A, B))

print("Multiplication:", matmul(A, B))

print("Scalar Addition:", scalarsum(scalar, A))
print("Scalar Subtraction:", scalarsub(scalar, A))

print("Normalization:", matnorm(A))