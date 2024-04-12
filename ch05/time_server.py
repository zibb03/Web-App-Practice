from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def display_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html_code = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>현재 시간 출력 앱</title>
        </head>
        <body>
            <h1>현재 시간: {current_time}</h1>
        </body>
    </html>
    """
    return html_code

if __name__ == '__main__':
    app.run(debug=True)