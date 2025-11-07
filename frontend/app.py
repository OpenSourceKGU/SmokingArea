from flask import Flask, render_template

app = Flask(__name__)

# '/' 경로로 접속하면 index.html 파일을 렌더링하여 반환
@app.route('/')
def home():
    # templates/index.html 파일을 찾아 렌더링합니다.
    return render_template('index.html')

if __name__ == '__main__':
    # 디버그 모드는 끄고, 0.0.0.0 주소의 5000번 포트로 실행
    # 0.0.0.0으로 설정해야 도커 컨테이너 외부에서 접근 가능합니다.
    app.run(host='0.0.0.0', port=5000)