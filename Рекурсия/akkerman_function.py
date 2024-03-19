def recursiya(m, n):
    if m == 0:
        return n+1 
    elif n == 0:
        return recursiya(m-1, 1)
    else:
        return recursiya(m -1, recursiya(m, n-1))
    
print(recursiya(22, 32))