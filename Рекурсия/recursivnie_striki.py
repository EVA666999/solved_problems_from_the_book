def recursiya(n):
    if n == 0:
        return 1
    else:
        recursiya(n-1)
        print('*'*n)

print(recursiya(5))