def recursiya(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + recursiya(arr[1:])
    
print(recursiya([2, 2, 3]))