my_dict = {'a': 98, 'b': 87, 'c': 92, 'd': 74, 'f': 89}
my_dict_copy = {k:v for (k,v) in my_dict.items() if v >= 90}
print(my_dict_copy)