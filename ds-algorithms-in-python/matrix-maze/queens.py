
#https://www.techiedelight.com/print-possible-solutions-n-queens-problem/

def is_queuens_threaten_each_other(mat, r, c):
 
    # return false if two queens share the same column
    for i in range(r):
        if mat[i][c] == 'Q':
            return True
 
    # return false if two queens share the same `` diagonal
    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if mat[i][j] == 'Q':
            return True
        i = i - 1
        j = j - 1
 
    # return false if two queens share the same `/` diagonal
    (i, j) = (r, c)
    while i >= 0 and j < len(mat):
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1
 
    return False


def n_queen(mat, r):

    if r == len(mat):
        print_solution(mat)
        return
    
    for i in range(len(mat)):

        if not is_queuens_threaten_each_other(mat, r, i):
            mat[r][i] = 'Q'
            n_queen(mat, r + 1)
            mat[r][i] = '-'

def print_solution(mat):
    for r in mat:
        print(str(r).replace(',', '').replace('\'', ''))
    print()


if __name__ == '__main__':

    N = 8

    mat = [['-' for x in range(N)] for y in range(N)]

    n_queen(mat, 0)