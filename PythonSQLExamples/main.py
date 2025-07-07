import sqlite3
import os

def create_database(): #database oluşturmak için
    if os.path.exists("students.db"): #Projenin bulunduğu yer.
        os.remove("students.db") # students.db databasei varsa sil.

    conn = sqlite3.connect("students.db") # database'e bağlantı yapar.
    cursor = conn.cursor() # databaseden veri okur, siler, ekleme yapar vs. SQL komutlarını okur.
    return conn, cursor

def create_tables(cursor): #cursor parametresi ister çünkü SQL komutlarını yazmamız için
    cursor.execute('''
    CREATE TABLE Students (
        id integer PRIMARY KEY,
        name varchar not null,
        age integer,
        email varchar UNIQUE,
        city varchar)
        
    ''')

    cursor.execute('''
    CREATE TABLE Courses (
        id integer PRIMARY KEY,
        course name varchar not null,
        instructor text,
        credit integer)

    ''')

def insert_sample__data(cursor):
    students = [
        (1,'Alice Johnson',20,'alice@gmail.com','New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chiago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle')
    ]

    cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)", students)

    courses = [
        (1, 'Python Programming', 'Dr.Anderson',3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr.Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2)
    ]

    cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)", courses)

    print("Samle data successfully inserted")

def basic_sql_operations(cursor):
    #1) Select All
    cursor.execute("SELECT * FROM Students") #datayı çektik
    records = cursor.fetchall() #dataları alacağımız fonksyion
    for row in records:
        print(f"ID: {row[0]} : Name: {row[1]} : Age: {row[2]} : email: {row[3]} city: {row[4]}") #print(row) deseydin de olurdu tuple içinde verirdi.
    print("-------------------------Select ALL---------------------")
    #2) Select Columns
    print("--------------------Select Columns----------------------")
    cursor.execute("SELECT name,age FROM Students")  # datayı çektik
    records = cursor.fetchall()  # dataları alacağımız fonksyion
    print(records)

    # 3) WHERE Clause --> Filtreleme
    print("--------------------WHERE age = 20----------------------")
    cursor.execute("SELECT * FROM Students WHERE age = 20")  # datayı çektik
    records = cursor.fetchall()  # dataları alacağımız fonksyion
    for row in records:
        print(row)

    # 4) WHERE with String
    print("--------------------WHERE City = New York----------------------")
    cursor.execute("SELECT name,age FROM Students WHERE city = 'New York'")  # datayı çektik
    records = cursor.fetchall()  # dataları alacağımız fonksyion
    print(records)

    # 5) Order by
    print("--------------------Order by age----------------------")
    cursor.execute("SELECT name,age FROM Students ORDER BY age")  # datayı çektik
    records = cursor.fetchall()  # dataları alacağımız fonksyion
    print(records)

    # 6) limit by
    print("--------------------limit by 3----------------------")
    cursor.execute("SELECT name,age FROM Students LIMIT 3")  # datayı çektik
    records = cursor.fetchall()  # dataları alacağımız fonksyion
    print(records)

def sql_update_delete_insert_operations(conn, cursor):
    #1)Insert
    cursor.execute("INSERT INTO Students VALUES (6,'Frank Miller', 23,'frank@gmail.com','Miami')")
    conn.commit() # daha sonrasında yapacağımız update işleminde hata çıkmaması için burada da commit ediyoruz.

    #2)Update
    cursor.execute("UPDATE Students SET age = 24 WHERE id = 6")
    conn.commit()  # daha sonrasında yapacağımız delete işleminde hata çıkmaması için burada da commit ediyoruz.

    #3)Delete
    cursor.execute("DELETE FROM Students WHERE id = 6")
    conn.commit()

def aggregate_functions(cursor):
    #1)Count
    print("------------------------------Aggregate functions Count---------------------")
    cursor.execute("SELECT COUNT(*) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    # 2) Average
    print("------------------------------Aggregate functions Average---------------------")
    cursor.execute("SELECT AVG(age) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    # 3) Max - Min
    print("------------------------------Aggregate functions Max - Min---------------------")
    cursor.execute("SELECT MAX(age), MIN(age) FROM Students")
    result = cursor.fetchone()
    print(result)

    # 4) GROUP BY
    print("------------------------------Aggregate functions Group By---------------------")
    cursor.execute("SELECT city, COUNT(*) FROM Students GROUP BY city")
    result = cursor.fetchall()
    print(result)


def main():
    conn, cursor = create_database() # hem database oluşturur hem de çalışmamız için bağlantıyı (conn) ve imleci (cursor) verir.
    try:
        create_tables(cursor)
        insert_sample__data(cursor)
        basic_sql_operations(cursor)
        sql_update_delete_insert_operations(conn, cursor)
        aggregate_functions(cursor)
        conn.commit() # cursor'ın yaptıklarını uygula.
    except sqlite3.Error as e:
        print(e) # hata varsa hata mesajını açıklar.
    finally:
        conn.close() # bağlantıyı ne olursa olsun kapatmak için



if __name__ == "__main__":
    main()