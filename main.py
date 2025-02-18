from flask import Flask, request
app = Flask(__name__)

# サーバールートへアクセスがあった時 --- (*1)
@app.route('/')
def index():
    # フォームを表示する --- (*2)
    return """
        <html><body>
        <form action="/hello" method="GET">
          名前: <input type="text" name="name">
          一言: <input type="text" name="message">
          <input type="submit" value="送信">
        </form>
        </body></html>
    """

# /hello へアクセスがあった時 --- (*3)
@app.route('/hello')
def hello():
    # nameのパラメータを得る --- (*4)
    name = request.args.get('name')
    if name is None: name = '名無し'
    message = request.args.get('message')
    if message is None: message = '特にありません'
    # 自己紹介を自動作成
    return """
    <h1>{0}さん、こんにちは！</h1>
    <p>一言: {1}</p>
    """.format(name, message)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

