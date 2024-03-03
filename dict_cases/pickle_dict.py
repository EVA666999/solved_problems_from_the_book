import pickle as p
my_dict = {1:'a', 2:'b'}
file = open('file.dat', 'wb')
p.dump(my_dict, file)
file.close()

def read():
    file = open('file.dat', 'rb')
    a = p.load(file)
    file.close()
    return a

print(read())
    