# 2.2
'''
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hi'

    
app.run(debug=True)
'''

# 3
'''
from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def index():
    return 'random : <strong>' + str(random.random())+'</strong>' # 문자열을 입력받음
    # 브라우저는 return 하는 HTML 코드만 해석

    
app.run(debug=True)
'''

# 4
# 라우팅

'''
from flask import Flask

app = Flask(__name__)

@app.route('/') # 사용자가 Path를 입력하지 않으면, 밑에 있는 함수를 실행하도록 하는 코드
def index(): # 라우팅
    return 'Welcome'


@app.route('/create/')
def create(): 
    # 위의 index 함수 관련 코드를 복사 붙여넣기 하다 보니, 함수명을 수정하지 않는 실수를 함
    # 관련 안내를 하면 좋을 듯함
    return 'Create'


@app.route('/read/<id>')
def read(id): # id를 함수에 파라미터로 제공
    print(id)
    return 'Read '+id


app.run(debug=True)
'''

# 5

"""
from flask import Flask

app = Flask(__name__)


# DB에서 데이터를 불러올 수 있는 부분
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

@app.route('/') 
def index(): 
    liTags = ''
    # for topic in topics:
    #     liTags = liTags + '<li>'+topic['title']+'</li>'
    # return '''<!doctype html>
    # <html>
    #     <body>
    #         <h1><a href="/">WEB</a></h1>
    #         <ol>
    #             <li><a href="/read/1/">html</a></li>
    #             <li><a href="/read/2/">css</a></li>
    #             <li><a href="/read/3/">javascript</a></li>
    #         </ol>
    #         <h2>Welcome</h2>
    #         Hello, Web
    #     </body>
    # </html>
    # '''

    for topic in topics:
            liTags = liTags + f'<li><a href=/read/{topic["id"]}>{topic["title"]}</a></li>'
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {liTags}
            </ol>
            <h2>Welcome</h2>
            Hello, Web
        </body>
    </html>
    '''


@app.route('/create/')
def create(): 
    return 'Create'


@app.route('/read/<id>')
def read(id): # id는 문자열(str)
    print(id)
    return 'Read '+id


app.run(debug=True)
"""

# 6

"""
from flask import Flask

app = Flask(__name__)


# DB에서 데이터를 불러올 수 있는 부분
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]


def template(contents, content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
        </body>
    </html>
    '''


def getContents():
    liTags = ''
    for topic in topics:
            liTags = liTags + f'<li><a href=/read/{topic["id"]}>{topic["title"]}</a></li>'
    return liTags


@app.route('/') 
def index(): 
    return template(getContents(), '<h2>Welcome<h2>Hello, Web')


@app.route('/read/<int:id>') #str인 id를 int로 바꿈
def read(id): 
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}')
    # return f'''<!doctype html>
    # <html>
    #     <body>
    #         <h1><a href="/">WEB</a></h1>
    #         <ol>
    #             {liTags}
    #         </ol>
    #         <h2>{title}</h2>
    #         {body}
    #     </body>
    # </html>
    # '''


@app.route('/create/')
def create(): 
    return 'Create'


app.run(debug=True)
"""

# 7.1

from flask import Flask

app = Flask(__name__)


topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]


def template(contents, content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href="/create/">create</a></li>
            </ul>    
        </body>
    </html>
    '''


def getContents():
    liTags = ''
    for topic in topics:
            liTags = liTags + f'<li><a href=/read/{topic["id"]}>{topic["title"]}</a></li>'
    return liTags


@app.route('/') 
def index(): 
    return template(getContents(), '<h2>Welcome<h2>Hello, Web')


@app.route('/read/<int:id>')
def read(id): 
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}')


@app.route('/create/')
def create():
    content = '''
        <form action="/create/" method="POST">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit" value="create"></p>
        </form>
    ''' 
    # 사용자가 입력한 정보를 서버로 전달하는 form
    # 서버의 어떤 경로로 전달할 것인지 나타내는 action - get 방식 전송(url을 통해)
    # 값을 변경할 때는 post 방식 - payloda(개발자 도구에서 확인 가능)를 통해 데이터를 감춤
    return template(getContents(), content)


app.run(debug=True)
