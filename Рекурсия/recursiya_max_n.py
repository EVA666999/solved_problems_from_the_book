def recursiya(my_list):
    if len(my_list) == 0:
        return float('-inf')
    else:
        max_rest = recursiya(my_list[:-1])
        return max(max_rest, my_list[-1])

print(recursiya([1, 2, 3, 4, 6]))
