import sqlite3

def create_table():
    # 데이터베이스를 연결하는 부분
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    # execute 함수를 통해 SQL 구문을 cursor에 전달하여 수행
    # students.db 를 생성하는 구문
    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                        (id INTEGER PRIMARY KEY, name TEXT, 
                        age INTEGER, major TEXT)''')
    
    # 데이터베이스의 변경사항을 저장하는 부분
    connection.commit()
    # 데이터베이스와의 연결을 종료하는 부분
    connection.close()

# create_table()

# 함수 실행 시 name, age, major에 해당하는 값을 받음
def insert_student(name, age, major):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    # 데이터를 주입하는 INSERT 구문
    cursor.execute('''INSERT INTO students (name, age, major)
                        VALUES (?, ?, ?)''', (name, age, major))
        
    connection.commit()
    connection.close()

# insert_student("john", 21, "computer science")

def query_students():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    # students 테이블의 모든 레코드를 선택하는(*) SELECT 구문
    cursor.execute("SELECT * FROM students")
    # 조회한 데이터를 저장하는 fetchall 함수
    rows = cursor.fetchall()

    connection.close()

    return rows

# print(query_students())

def update_student(student_id, name, age, major):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    # 주어진 id를 가진 레코드의 정보를 갱신하는 UPDATE 구문
    cursor.execute('''UPDATE students SET name = ?,
                   age = ?, major = ? WHERE id = ?''',
                   (name, age, major, student_id))

    connection.commit()
    connection.close()

# update_student(1, "john", 22, "Data Science")
# print(query_students())

def delete_student(student_id):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    # 주어진 id를 가진 레코드의 정보를 삭제하는 DELETE 구문
    cursor.execute("DELETE FROM students WHERE id = ?",
                   (student_id,))

    connection.commit()
    connection.close()

# delete_student(1)
print(query_students())