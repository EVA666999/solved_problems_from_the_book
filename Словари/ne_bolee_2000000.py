my_dict = {1: 8398748, 2: 1398748, 3: 2398748, 4: 1398748, 5: 4398748, 6: 1398748, 7: 5398748, }
my_dict_copy = {k:v for (k,v) in my_dict.items() if v > 2000000}
print(my_dict_copy)