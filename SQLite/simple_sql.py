import sqlite3

def main():
    conn = sqlite3.connect('Book.db')

    cur = conn.cursor()

    cur.execute('''CREATE TABLE  IF NOT EXISTS Book (Izdatel TEXT,
                Name TEXT,
                Pages INTEGER,
                Simbolscode, TEXT)''')
    
    conn.commit()
    cur.execute('DROP TABLE IF EXISTS Book')
    conn.close()    

if __name__ == '__main__':
    main()