def pow(a, b):
 
    if b == 0:
        return 1
 
    power = pow(a, b - 1)
 
    result = 0
    for i in range(a):
        result += power
 
    return result
 
 
if __name__ == '__main__':
 
    print(pow(7, 3))
 