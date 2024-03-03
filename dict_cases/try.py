my_str = 'We observe today not a victory a'
my_str = my_str.split()
a = [i for i in my_str]
d = {}
for index, a in enumerate(my_str):
    d.setdefault(a, []).append(index)
print(d)


    # my_dict1 = {}
    # for index, realy_split_string in enumerate(realy_split_string):
    #     my_dict1.setdefault(realy_split_string, []).append(index)
    # return my_dict1