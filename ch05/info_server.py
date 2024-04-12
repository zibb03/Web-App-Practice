# 플라스크 모듈을 불러오는 부분
from flask import Flask

# 플라스크 객체를 생성하는 부분
app = Flask(__name__)

# 함수와 URL(/)을 연결해 주는 route 데코레이터
@app.route('/')
def about_flask():
    return f"""
    <!-- HTML 문서의 제목을 나타내는 <h1> 태그 -->
    <h1>플라스크의 특징</h1>

    <!-- 순서가 없는 목록을 나타내는 <ul> 태그 -->
    <ul>
        <!-- 목록(List)을 나타내는 <li> 태그 -->
        <!-- 텍스트를 굵게 바꾸어주는 <strong> 태그 -->
        <li><strong>가볍고 민첩함</strong></li>
        <!-- 단락(Paragraph)을 나타내는 <p> 태그 -->
        <p>
            플라스크는 간단한 기본 구조를 가지고 있어 작은 웹 애플리케이션에 적합합니다.
        </p>
        <li><strong>확장성</strong></li>
        <p>
            플라스크는 다양한 확장을 사용하여 기능을 더할 수 있어, 프로젝트가 성장함에 따라 쉽게 확장할 수 있습니다.
        </p>
        <li><strong>유연함</strong></li>
        <p>
            플라스크는 개발자가 원하는 방식으로 웹 애플리케이션을 구성할 수 있도록 해줍니다.
        </p>
    </ul>
    """

# 프로그램의 시작 지점을 알려주는 메인 함수
if __name__ == '__main__':
    # 플라스크를 실행하는 run 함수
    app.run()