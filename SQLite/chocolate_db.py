import sqlite3


def main():
    again = 'д'
    con = sqlite3.connect('chocolate.db')

    cur = con.cursor()

    cur.execute('''UPDATE Chocolate
                   SET PRICE = 4.99''')
    
    con.commit()
    print(cur.rowcount)
    con.close()

if __name__ == '__main__':
    main()