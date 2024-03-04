import class_pet

def main():

    name = input('Введите имя: ')
    animal_type = input('Введите тип: ')
    age = int(input('Введите возраст: '))

    obj = class_pet.Pet(name, animal_type, age)

    obj.set_name(name)
    obj.set_animal_type(animal_type)
    obj.set_age(age)

    print(f'{obj.__str__()}')

if __name__ == '__main__':
    main()
