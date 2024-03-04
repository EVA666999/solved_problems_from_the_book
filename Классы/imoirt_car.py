import class_car

def main():
    year_model = input('Введите год модели: ')
    make = input('Введите фирму изготовителя: ')
    for _ in range(1, 6):
        speed = int(input('Введите начальную скорость: '))
        obj = class_car.Car(year_model, make, speed)
        obj.set_accelerate(speed)
        print(f'{obj.str_accelerate()}')

    for _ in range(1, 6):
        speed = int(input('Введите начальную скорость: '))
        obj = class_car.Car(year_model, make, speed)
        obj.set_break_speed()
        print(f'{obj.str_break()}')

if __name__ == '__main__':
    main()
