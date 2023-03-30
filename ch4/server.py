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

"""
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
    # 값을 변경할 때는 post 방식 - paylode(개발자 도구에서 확인 가능)를 통해 데이터를 감춤
    return template(getContents(), content)


app.run(debug=True)
"""

# 7.2

"""
from flask import Flask, request, redirect # request를 확인하기 위함


app = Flask(__name__)

nextId = 4
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


@app.route('/read/<int:id>/') # 끝에 / 붙여야 함.
def read(id): 
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}')


@app.route('/create/', methods=['GET', 'POST']) # 라우터가 허용하는 method를 적용해야 함
def create():
    # 요청한 것이 get인지 post인지 구분하는 request.method
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        # 사용자가 입력한 정보를 서버로 전달하는 form
        # 데이터를 주고받는 방식(get, post)
        # 서버의 어떤 경로로 전달할 것인지 나타내는 action - get 방식 전송(url을 통해)
        # 값을 변경할 때는 post 방식 - paylode(개발자 도구에서 확인 가능)를 통해 데이터를 감춤
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        # request object
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id': nextId, 'title': title, 'body': body}
        topics.append(newTopic)
        print(topics)
        url = '/read/'+str(nextId)+'/'
        nextId = nextId + 1
        return redirect(url)

app.run(debug=True)
"""

# 8

"""
from flask import Flask, request, redirect # request를 확인하기 위함


app = Flask(__name__)

nextId = 4
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]


def template(contents, content, id=None):
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li><a href="/update/{id}/">update</a></li>
        '''
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
                {contextUI}
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


@app.route('/read/<int:id>/')
def read(id): 
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}', id)


@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id': nextId, 'title': title, 'body': body}
        topics.append(newTopic)
        print(topics)
        url = '/read/'+str(nextId)+'/'
        nextId = nextId + 1
        return redirect(url)
    

@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        title = ''
        body = ''
        for topic in topics:
            if id == topic['id']:
                title = topic['title']
                body = topic['body']
                break
        content = f'''
            <form action="/update/{id}/" method="POST">
                <p><input type="text" name="title" placeholder="title" value="{title}"></p>
                <p><textarea name="body" placeholder="body">{body}</textarea></p>
                <p><input type="submit" value="update"></p>
            </form>
        '''
        # title값을 value로 전달
        return template(getContents(), content)
    elif request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        for topic in topics:
            if id == topic['id']:
                topic['title'] = title
                topic['body'] = body
                break
        url = '/read/'+str(id)+'/'
        return redirect(url)

app.run(debug=True)
"""

# 9

from flask import Flask, request, redirect # request를 확인하기 위함


app = Flask(__name__)

nextId = 4
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]


def template(contents, content, id=None):
    contextUI = ''
    if id != None:
        # delete url로 접속해도 삭제가 되지 않도록 함 - get 방식이어서
        # 임의로 post 방식으로 보내면 삭제되긴 함 
        contextUI = f'''
            <li><a href="/update/{id}/">update</a></li>
            <li><form action="/delete/{id}" method="POST"><input type="submit" value="delete"></form></li>
        '''
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
                {contextUI}
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


@app.route('/read/<int:id>/')
def read(id): 
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}', id)


@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id': nextId, 'title': title, 'body': body}
        topics.append(newTopic)
        print(topics)
        url = '/read/'+str(nextId)+'/'
        nextId = nextId + 1
        return redirect(url)
    
    
@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        title = ''
        body = ''
        for topic in topics:
            if id == topic['id']:
                title = topic['title']
                body = topic['body']
                break
        content = f'''
            <form action="/update/{id}/" method="POST">
                <p><input type="text" name="title" placeholder="title" value="{title}"></p>
                <p><textarea name="body" placeholder="body">{body}</textarea></p>
                <p><input type="submit" value="update"></p>
            </form>
        '''
        # title값을 value로 전달
        return template(getContents(), content)
    elif request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        for topic in topics:
            if id == topic['id']:
                topic['title'] = title
                topic['body'] = body
                break
        url = '/read/'+str(id)+'/'
        return redirect(url)


@app.route('/delete/<int:id>/', methods=['POST']) # POST 방식만 허용하도록 함
def delete(id):
    for topic in topics:
        if id == topic['id']:
            topics.remove(topic) #topic이라는 값(인자)을 topics에서 제거함
            break
    return redirect('/')


app.run(debug=True)