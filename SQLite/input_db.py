import sqlite3

def main():

    again = 'д'

    conn = sqlite3.connect('Inventory.db')

    cur = conn.cursor()

    while again == 'д':
        item_name = input('Название: ')
        price = float(input('Цена: '))

        cur.execute('''INSERT INTO Inventory (ItemName, price)
                       VALUES (?, ?)''',
                       (item_name, price))
        
        again = input('Добавить ещё одну позицию? (д/н): ')

    conn.commit()

    conn.close()


if __name__ == '__main__':
    main()