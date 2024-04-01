import sqlite3

def main():
    ADD = 1
    FOUND = 2
    UPDATE = 3
    DEL = 4
    SHOW = 5
    ADD_FACULTET = 6
    FOUND_F = 7
    UPDATE_F = 8
    DEL_F = 9
    SHOW_F = 10
    ADD_S = 11
    FOUND_S = 12
    UPDATE_S = 13
    DEL_S = 14
    SHOW_S = 15
    EXIT = 0

    con = sqlite3.connect('Students.db')
    cur = con.cursor()

    choise = input('Выбирите номер из меню: ')

    while choise != EXIT:
        if choise == ADD:
            print(add(cur, con))
        elif choise == FOUND:
            print(found(cur))
        elif choise == FOUND_F:
            print(found_f(cur))
        elif choise == FOUND_S:
            print(found_s(cur))
        elif choise == UPDATE:
            print(update(cur, con))
        elif choise == UPDATE_F:
            print(update_f(cur, con))
        elif choise == UPDATE_S:
            print(update_s(cur, con))
        elif choise == DEL:
            print(delete(cur, con))
        elif choise == DEL_F:
            print(delete_f(cur, con))
        elif choise == DEL_S:
            print(delete_s(cur, con))
        elif choise == SHOW:
            print(show(cur))
        elif choise == SHOW_F:
            print(show_f(cur))
        elif choise == SHOW_F:
            print(show_s(cur))
        elif choise == ADD_FACULTET:
            print(add_f(cur, con))
        elif choise == ADD_S:
            print(add_s(cur, con))
        elif choise == EXIT:
            return 
        choise = int(input('Введите номер из меню: '))


def add(cur, con):
    name = input('Введите имя новой специальности: ')
    cur.execute('PRAGMA foreign_key=ON')
    cur.execute('''INSERT INTO Majors
                (Name)
                VALUES(?)''',
                (name,))
    con.commit()
    return "Специальность успешно добавлена."

def add_f(cur, con):
    name = input('Введите имя нового факультета: ')
    cur.execute('PRAGMA foreign_key=ON')
    cur.execute('''INSERT INTO Students.Name
                (Name)
                VALUES(?)''',
                (name,))
    con.commit()
    return "факультет успешно добавлена."

def add_s(cur, con):
    name = input('Введите имя нового студента: ')
    major_id = int(input('Введите ID специальности для студента: '))
    dept_id = int(input('Введите ID факультета для студента: '))
    
    cur.execute('SELECT Name FROM Majors WHERE MajorID=?', (major_id,))
    major_name = cur.fetchone()
    if not major_name:
        return "Ошибка: Специальность с таким ID не существует."
    
    cur.execute('SELECT Name FROM Departaments WHERE DeptID=?', (dept_id,))
    dept_name = cur.fetchone()
    if not dept_name:
        return "Ошибка: Факультет с таким ID не существует."
    
    cur.execute('INSERT INTO Students (Name, MajorID, DeptID) VALUES (?, ?, ?)', (name, major_id, dept_id))
    con.commit()
    
    return "Студент успешно добавлен."

def found(cur):
    ask = input('Введите специальность, которую хотите найти: ')
    cur.execute('PRAGMA foreign_key=ON')
    cur.execute('''SELECT Majors.Name
                   FROM Majors
                   WHERE Name LIKE ?''', ('%' + ask + '%',))
    rows = cur.fetchall()
    return rows

def found_f(cur):
    ask = input('Введите факультет, который хотите найти: ')
    cur.execute('PRAGMA foreign_key=ON')
    cur.execute('''SELECT Departaments.Name
                   FROM Departaments
                   WHERE Name LIKE ?''', ('%' + ask + '%',))
    rows = cur.fetchall()
    return rows

def found_s(cur):
    name = input('Введите студента, котрого хотите найти: ')
    cur.execute('PRAGMA foreign_key=ON')
    cur.execute('''SELECT Students.Name
                   FROM Students
                   WHERE Name LIKE ?''', ('%' + name + '%',))
    rows = cur.fetchall()
    return rows

def update(cur, con):
    ask = input('Введите специальность, которую хотите обновить: ')
    new_name = input('Введите новое название специальности: ')
    cur.execute('PRAGMA foreign_key=ON')
    cur.execute('''UPDATE Majors
                   SET Name = ?
                   WHERE Name LIKE ?''', (new_name, '%' + ask + '%'))
    con.commit()
    rows = cur.fetchall()
    return rows

def update_f(cur, con):
    ask = input('Введите факультет, которую хотите обновить: ')
    new_name = input('Введите новое название факультета: ')
    cur.execute('PRAGMA foreign_key=ON')
    cur.execute('''UPDATE Departaments
                   SET Name = ?
                   WHERE Name LIKE ?''', (new_name, '%' + ask + '%'))
    con.commit()
    rows = cur.fetchall()
    return rows

def update_s(cur, con):
    ask = input('Введите студента, которого хотите обновить: ')
    new_name = input('Введите новое имя студента: ')
    cur.execute('PRAGMA foreign_key=ON')
    cur.execute('''UPDATE Students
                   SET Name = ?
                   WHERE Name LIKE ?''', (new_name, '%' + ask + '%'))
    con.commit()
    rows = cur.fetchall()
    return rows

def delete(cur, con):
    ask = input('Введите специальность которую хотите удалить: ')
    cur.execute('PRAGMA foreign_key=ON')
    cur.execute('''DELETE FROM Majors
                   WHERE Name LIKE ?''', ('%' + ask + '%',))
    con.commit()
    rows = cur.fetchall()
    return rows

def delete_f(cur, con):
    ask = input('Введите факультет который хотите удалить: ')
    cur.execute('PRAGMA foreign_key=ON')
    cur.execute('''DELETE FROM Departaments
                   WHERE Name LIKE ?''', ('%' + ask + '%',))
    con.commit()
    rows = cur.fetchall()
    return rows

def delete_s(cur, con):
    name = input('Введите студента которого хотите удалить: ')
    cur.execute('PRAGMA foreign_key=ON')
    cur.execute('''DELETE FROM Students
                   WHERE Name LIKE ?''', ('%' + name + '%',))
    con.commit()
    rows = cur.fetchall()
    return rows

def show(cur):
    cur.execute('PRAGMA foreign_key=ON')
    cur.execute('''SELECT * FROM Majors''')
    rows = cur.fetchall()
    return rows

def show_f(cur):
    cur.execute('PRAGMA foreign_key=ON')
    cur.execute('''SELECT * FROM Departaments''')
    rows = cur.fetchall()
    return rows

def show_s(cur):
    cur.execute('PRAGMA foreign_key=ON')
    cur.execute('''SELECT * FROM Students''')
    rows = cur.fetchall()
    return rows

if __name__ == '__main__':
    main()