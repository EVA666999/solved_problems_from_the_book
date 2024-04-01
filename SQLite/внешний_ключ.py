import sqlite3

def main():

    con = sqlite3.connect('Students.db')

    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS Majors(
                MajorID INTEGER PRIMARY KEY NOT NULL,
                Name TEXT)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS Departaments(
                DeptID INTEGER PRIMARY KEY NOT NULL,
                Name TEXT)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS Students(
                StudentID INTEGER PRIMARY KEY NOT NULL,
                Name TEXT,
                MajorID INTEGER,
                DeptID INTEGER,
                FOREIGN KEY (MajorID) REFERENCES Majors(MajorID),
                FOREIGN KEY (DeptID) REFERENCES Departaments(DeptID)
                )""")
    
    con.commit()
    con.close()

if __name__ == '__main__':
    main()