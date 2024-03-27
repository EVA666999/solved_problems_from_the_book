import sqlite3

def main():

    con = sqlite3.connect('cities.db')

    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS cities(
                CityID INTEGER PRIMARY KEY NOT NULL,
                CityName TEXT,
                Population REAL)""")
    
    con.commit()
    con.close()

if __name__ == '__main__':
    main()