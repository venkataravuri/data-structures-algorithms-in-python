
# https://www.tutorialcup.com/interview/matrix/unique-paths.htm

# Find the number of unique paths that can be taken to reach 
# a cell located at (m,n) from the cell located at (1,1) 
# given that you can move downwards or rightwards only.

# Bottom-up space-efficient function to count all paths from the first
# cell (0, 0) to the last cell (M-1, N-1) in a given `M × N` rectangular grid
def countPaths(m, n):
 
    T = [0] * N
    
    T[0] = 1
 
    # fill `T` in a bottom-up manner
    for i in range(m):
        for j in range(1, n):
            T[j] = T[j] + T[j - 1]
 
    # return the last cell
    return T[n-1]
 
 
if __name__ == '__main__':
 
    # `M × N` matrix
    M = N = 3
 
    k = countPaths(M, N)
    print("The total number of paths is", k)