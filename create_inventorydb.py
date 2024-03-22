import sqlite3


def main():

    con = sqlite3.connect('Inventory.db')

    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS Inventory(
                ItemID INTEGER PRIMARY KEY NOT NULL,
                ItemName TAEXT,
                Price REAL)""")
    
    con.commit()
    con.close()

if __name__ == '__main__':
    main()