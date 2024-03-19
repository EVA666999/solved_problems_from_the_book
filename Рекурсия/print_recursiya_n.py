def recursiya(n):
    if n > 0:
        recursiya(n-1)
        print(n)
    
print(recursiya(10))