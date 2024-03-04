import pickle
import cellphonel

FILENAME = 'cellphones.dat'

def main():
    ask = 'д'
    
    file = open(FILENAME, 'wb')

    while ask.lower() == 'д':
        man = input('Производитель: ')
        mod = input('Модель: ')
        price = int(input('Цена: '))
        phone = cellphonel.Chellphone(man, mod, price)
        pickle.dump(phone, file)
        ask = input('Ввести ещё данные? ')

    file.close()

if __name__ == '__main__':
    main()