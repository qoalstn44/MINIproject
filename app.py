from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://songjihyun323:dan0118@cluster0.agyqtp5.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

## 방명록 등록
@app.route("/onebillion", methods=["POST"])
def comment_post():
    nickname_receive = request.form['nickname_give']
    password_receive = request.form['password_give']
    comment_receive = request.form['comment_give']
    time_receive = request.form['time_give']

    doc = {
        "nickname": nickname_receive,
        "password": password_receive,
        "comment": comment_receive,
        "time": time_receive
    }
    db.onebillion.insert_one(doc)

    return jsonify({'msg': '방명록을 작성했습니다!'})

## 방명록 가져오기
@app.route('/onebillion', methods=['GET'])
def comment_get():
    comment_list = list(db.onebillion.find({}, {'_id':False}))
    return jsonify({'comments': comment_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)