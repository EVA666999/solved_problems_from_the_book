def recursiya(n, stepeny_n):
    if stepeny_n == 1:
        return n
    else:
        return n * recursiya(n, stepeny_n-1)
    

print(recursiya(2, 4))