def find_max_square(matrix):
    rows, columns = len(matrix), len(matrix[0])
    result = 0
    dp = [[0 for _ in range(columns)] for _ in range(rows)]

    for row in range(rows):
        for column in range(columns):
            if row == 0 or column == 0:
                dp[row][column] = matrix[row][column]
            elif matrix[row][column] == 0:
                dp[row][column] = 0
            else:
                dp[row][column] = 1 + min(dp[row][column -1], dp[row -1][column-1], dp[row -1][column])
                result = max(result, dp[row][column])

    return result


if __name__ == '__main__':

    matrix = [[1, 1, 0, 1, 0, 0], [1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 0], [0, 0, 1, 1, 1, 0]]

    print(find_max_square(matrix))