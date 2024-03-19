def func(x, y):
    if x % y == 0:
        return y
    else:
        return func(x, x % y)

print(func(49, 28))