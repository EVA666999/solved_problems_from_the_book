my_dict = {'п':'.._..', 'р':'!!'}

my_str = 'привет'
a = my_str
for i in my_str:
    for key, value in my_dict.items():
        if i == key:
            a = a.replace(i, value)
print(a)
