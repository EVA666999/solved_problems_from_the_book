import sqlite3

def main():

    conn = sqlite3.connect('cities.db')

    cur = conn.cursor()

    cityname = ['a', 's', 'f', 'd', 'ee', 'ff', 'dds', 'fgg']
    population = [1, 3, 2, 5, 6, 7, 55, 33]
    
    for i, j in zip(cityname, population):
        cur.execute('''INSERT INTO cities (CityName, Population)
                VALUES (?, ?)''',
                (i, j))

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()