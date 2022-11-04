from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://songjihyun323:dan0118@cluster0.agyqtp5.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

## 방명록 등록 송지현 작성
@app.route("/onebillion", methods=["POST"])
def comment_post():
    nickname_receive = request.form['nickname_give']
    comment_receive = request.form['comment_give']
    time_receive = request.form['time_give']

    doc = {
        "nickname": nickname_receive,
        "comment": comment_receive,
        "time": time_receive
    }
    db.onebillion.insert_one(doc)

    return jsonify({'msg': '방명록을 작성했습니다!'})

## 방명록 가져오기 송지현 작성
@app.route('/onebillion', methods=['GET'])
def comment_get():
    comment_list = list(db.onebillion.find({}, {'_id':False}))
    return jsonify({'comments': comment_list})

# 팀원추가 성태영 작성
@app.route("/team", methods=["POST"])
def team_post():
    teams_receive = request.form['teams_give']
    intro_receive = request.form['intro_give']
    photo_recevie = request.form['photo_give']
    team_list = list(db.oneBillion.find({}, {'_id': False}))
    count = len(team_list) + 1

    doc = {
        'like':0,
        'teams':teams_receive,
        'intro': intro_receive,
        'num':count,
        'photo':photo_recevie
    }
    db.oneBillion.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})

# 좋아요수 post 성태영 작성
@app.route("/api/like", methods=["POST"])
def like_post():
    num_receive = request.form['num_give']
    target_star = db.oneBillion.find_one({'num': int(num_receive)})
    current_like = target_star['like']
    new_like = current_like + 1
    db.oneBillion.update_one({'num': int(num_receive)}, {'$set': {'like': new_like}})
    return jsonify({'msg': '좋아요 +1'})

# 추가된 팀원 get 성태영 작성
@app.route("/team", methods=["GET"])
def team_get():
    teams_list = list(db.oneBillion.find({}, {'_id': False}))
    return jsonify({'teams': teams_list})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)