
# Function to find the nth Fibonacci number
def fib(n, lookup):
 
    if n <= 1:
        return n
 
    # if the subproblem is seen for the first time
    if n not in lookup:
        lookup[n] = fib(n - 1, lookup) + fib(n - 2, lookup)
 
    return lookup[n]
 
 
if __name__ == '__main__':
 
    n = 8
    lookup = {}
 
    print('F(n) =', fib(n, lookup))