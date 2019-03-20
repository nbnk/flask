# モジュールの読み込み
from flask import Flask, jsonify, abort, make_response

# Flaskクラスのインスタンスを作成
app = Flask(__name__)

# GETの実装
@app.route('/get', methods=['GET'])
def get():
    result = { "greeting": 'hello flask' }
    return make_response(jsonify(result))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
