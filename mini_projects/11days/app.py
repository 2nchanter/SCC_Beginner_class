from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.teampj


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

# 2
# # 이벤트 이름, 날짜 선택 (POST) API
# @app.route('/events', methods=['POST'])
# def save_event():
#     name_receive = request.form['name_give']
#     # dates_receive = request.form['dates_give'] 날짜
#
#     doc = {
#         'title': name_receive,
#         # 'dates': dates_receive,
#     }
#     db.events.insert_one(doc)
#     return jsonify({'result': 'success', 'msg': '이벤트가 생성되었습니다!'})
#
#
# # UserName(POST) API
# @app.route('events', methods=['POST'])
# def save_event():
#     eventname_receive = request.form['name_give']
#     dates_receive = request.form['dates_give']
#
#     doc = {
#         'eventname': eventname_receive,
#         'dates': dates_receive,
#     }
#     db.orders.insert_one(doc)
#     return jsonify({'result': 'success', 'msg': '주문 완료!'})


## API 역할을 하는 부분
@app.route('/events', methods=['POST'])
def add_user():
    user_receive = request.form['user_give']


    doc = {
        'user':user_receive
    }

    db.teampj.insert_one(doc)

    print(sample_receive)
    return jsonify({'msg': '이벤트 저장 완료!'})

@app.route('/events', methods=['GET'])
def show_users():
    events = list(db.teampj.find({}, {'_id': False}))
    return jsonify({'all_events': events})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
