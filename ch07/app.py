# index.html과 함께 읽으면 좋습니다.

# Flask와 SQLite 모듈을 불러오는 부분
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                        (id INTEGER PRIMARY KEY, task TEXT)''')
    connection.commit()
    connection.close()

# 함수와 URL(/)을 연결해 주는 route 데코레이터
@app.route('/')
def index():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    connection.close()
    # templates 폴더에 저장된 index.html을 불러오는 부분
    return render_template('index.html', tasks=tasks)

# index.html의 <form> 태그를 통해 새로운 정보를 받아오는 POST 방식
@app.route('/add', methods=['POST'])
def add_task():
    # <form> 태그에서 보낸 작업명을 task 변수에 저장하는 코드
    task = request.form['task']
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    connection.commit()
    connection.close()
    # index 함수로 연결해주는 부분
    return redirect(url_for('index'))

# <a> 태그의 task[0] 값을 정수형 변수 task_id의 인자로 받아오는 부분
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    connection.commit()
    connection.close()
    # index 함수로 연결해주는 부분
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)