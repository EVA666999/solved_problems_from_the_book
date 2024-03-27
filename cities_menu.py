import sqlite3

def main():
    '''Сортировка по численности населения в порядке возрастания'''
    SORT1 = 1
    '''Сортировка по численности населения в порядке убывания'''
    SORT2 = 2
    '''Вывод городов отсортированых по названию'''
    SITY_SORT1 = 3
    '''Общая численность населения'''
    COUNT_POPULATION = 4
    '''Средняя численность населения'''
    AVG_POPULATION = 5
    '''Город с найбольшим населением'''
    MAX_CITY_POPULATION = 6
    '''Город с наименьшим населением'''
    MIN_CITY_POPULATION = 7
    '''Выход'''
    EXIT = 8
    con = sqlite3.connect('cities.db')
    cur = con.cursor()

    choise = int(input('Введите номер из меню: '))
    while choise != EXIT:
        if choise == SORT1:
            print(sort1(cur))
        elif choise == SORT2:
            print(sort2(cur))
        elif choise == SITY_SORT1:
            print(sity_sort1(cur))
        elif choise == COUNT_POPULATION:
            print(count_population(cur))
        elif choise == AVG_POPULATION:
            print(avg_population(cur))
        elif choise == MAX_CITY_POPULATION:
            print(max_city_pop(cur))
        elif choise == MIN_CITY_POPULATION:
            print(min_city_pop(cur))
        elif choise == EXIT:
            return 
        choise = int(input('Введите номер из меню: '))

    con.close()

def sort1(cur):
    cur.execute('''SELECT CityName, Population
                   FROM cities
                   ORDER BY Population''')
    rows = cur.fetchall()
    return rows

def sort2(cur):
    cur.execute('''SELECT CityName, Population
                   FROM cities
                   ORDER BY Population DESC''')
    rows = cur.fetchall()
    return rows

def sity_sort1(cur):
    cur.execute('''SELECT CityName
                   FROM cities
                   ORDER BY CityName''')
    rows = cur.fetchall()
    return rows

def count_population(cur):
    cur.execute('''SELECT Population
                   FROM cities''')
    rows = cur.fetchall()
    populations = [row[0] for row in rows]
    
    # Суммируем числовые значения населения
    total_population = sum(populations)
    
    return total_population

def avg_population(cur):
    cur.execute('''SELECT AVG(Population)
                   FROM cities''')
    rows = cur.fetchall()
    
    return rows

def max_city_pop(cur):
    cur.execute('''SELECT CityName
               FROM cities
               WHERE Population = (SELECT MAX(Population) FROM cities)''')
    rows = cur.fetchall()
    
    return rows

def min_city_pop(cur):
    cur.execute('''SELECT CityName
               FROM cities
               WHERE Population = (SELECT MIN(Population) FROM cities)''')
    rows = cur.fetchall()
    
    return rows

if __name__ == '__main__':
    main()
