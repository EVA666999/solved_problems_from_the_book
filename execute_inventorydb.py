import sqlite3

def main():

    con = sqlite3.connect('Inventory.db')

    cur = con.cursor()

    cur.execute('''INSERT INTO Inventory (ItemName, Price)
                VALUES ('Молоко', 4.99)''')
    cur.execute('''INSERT INTO Inventory (ItemName, Price)
                VALUES ('Отвёртка', 2.99)''')
    cur.execute('''INSERT INTO Inventory (ItemName, Price)
                VALUES ('Плоскогубцы', 10.99),
                       ('Крем', 4.33),
                       ('Мыло', 43.33)''')
    
    con.commit()

    con.close()

if __name__ == '__main__':
    main()