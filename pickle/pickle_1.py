import pickle

def write():
    text = 'abvv'
    my_dict = {1: 'a', 2: 'b'}
    file = open('file.dat', 'wb')
    pickle.dump(my_dict, file)
    pickle.dump(text, file)
    file.close()

print(write())

def read():
    file = open('file.dat', 'rb')
    pb = pickle.load(file)
    print(pb)
    file.close()

print(read())