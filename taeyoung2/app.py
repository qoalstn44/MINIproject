from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.xwjtxso.mongodb.net/?retryWrites=true&w=majority', tlsCaFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/like', methods=['GET'])
def test_get():
    like_list = list(db.mini.find({}, {'_id': False}))
    return jsonify({'likes': like_list})



@app.route('/like', methods=['POST'])
def like_star():
    name_receive = request.form['name_give']

    target_star = db.mystar.find_one({'name': name_receive})
    current_like = target_star['like']

    new_like = current_like + 1

    db.mini.update_one({'name': name_receive}, {'$set': {'like': new_like}})

    return jsonify({'msg': '좋아요 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
