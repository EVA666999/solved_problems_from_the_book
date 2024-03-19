def recursiya(n):
    if n == 0:
        return 0
    else:
        return n + recursiya(n-1)
    
print(recursiya(2))