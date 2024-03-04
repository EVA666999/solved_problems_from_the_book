import pickle
import cellphonel


FILENAME = 'cellphones.dat'

def main():
    file = open(FILENAME, 'rb')
    end = False
    while not end:
        try:
            phone = pickle.load(file)
            display_data(phone)
        except EOFError:
            end = True
    file.close()

def display_data(phone):
    print(f'Производитель: {phone.get_manufact()}')
    print(f'Модель: {phone.get_model()}')
    print(f'Цена: {phone.get_retail_price()}')
    print()

if __name__ == '__main__':
    main()