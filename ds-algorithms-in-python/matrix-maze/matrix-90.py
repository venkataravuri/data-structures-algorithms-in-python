


def transpose(matrix):
    n = len(matrix)
    for row in range(n//2):
        for column in range(row, n - row - 1):
            temp =  matrix[row][column]
            matrix[row][column] = matrix[column][n - 1 - row]
            matrix[column][n - 1 - row] = matrix[n - 1 - row][n - 1 - column]
            matrix[n - 1 - row][n - 1 - column] = matrix[n - 1 - column][row]
            matrix[n - 1 - column][row] = temp

    return matrix

def printMatrix(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            print(f"{matrix[row][column]}", end=" ")
        print()

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Original Matrix")
    printMatrix(matrix)
    print("Transposed Matrix")
    printMatrix(transpose(matrix))
