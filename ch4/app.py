from flask import Flask
app = Flask(__name__)


topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascruot', 'body': 'javascript is ...'}
]


@app.route('/')
def index():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return f'''<!DOCTYPE html>
<html>
    <head>     
        <title>HTML</title>
        <!-- 웹페이지의 제목을 나타내는 <title> 태그 -->
    </head>
    <body>
        <h1>Web Application</h1>
        <!-- HTML 문서의 제목을 나타내는 <h1> 태그 -->
        <!-- 폰트의 크기가 클수록 낮은 숫자(1 ~ 6)로 나타냄 -->
        <ol>
        <!-- 순서가 있는 목록을 나타내는 <ol> 태그 -->
            <li>HTML</li>
            <li>Internet</li>
            <li>Python</li>
            <li>Flask</li>
            <li>MySQL</li>
            <li>Cloud Service</li>  
            <!-- 목록(List)을 나타내는 <li> 태그 -->       
        </ol>
        <ul>
        <!-- 순서가 없는 목록을 나타내는 <ul> 태그 -->
            <li>HTML</li>
            <p>
            <!-- 단락(Paragraph)을 나타내는 <p> 태그 -->
                The <strong>HyperText Markup Language</strong>(or HTML) is the standard markup language for documents designed to be displayed in a <u>web browser</u>.<br>
                It is often assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript.
                <!-- 텍스트를 굵게 바꾸어주는 <strong> 태그 -->
                <!-- 텍스트에 밑줄(underline)을 그어주는 <u> 태그 -->
                <!-- 줄 바꿈(Line Break)을 실시하는 <br> 태그 -->
            </p>    
            <img src="image_1.jpg" alt="HTML" width="30%">
            <!-- 사진(image)를 나타내는 <img> 태그 -->
            <!-- 이미지의 경로를 나타내는 src 속성 -->
            <!-- 이미지의 설명을 나타내는 alt 속성 -->
            <!-- 이미지의 크기를 지정하는 width 속성 -->
            <h3><a href="index.html">Back</a></h3>
            <!-- HTML 문서의 제목을 나타내는 <h3> 태그 -->
            <!-- 폰트의 크기가 클수록 낮은 숫자(1 ~ 6)로 나타냄 -->
            <!-- 현재 문서와 다른 문서를 연결하는 <a> 태그 -->
            <!-- 연결할 문서를 나타내는 href 속성 -->
        </ul>
    </body>   
</html>

    '''


@app.route('/create/')
def create():
    return 'Create'


@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'Read '+id

app.run(port=5001)