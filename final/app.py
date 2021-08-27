from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbhomework

## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    adrs_receive = request.form['adrs_give']
    sgnt_receive = request.form['sgnt_give']
    tel_receive = request.form['tel_give']

    doc = {
        'name':name_receive,
        'adrs':adrs_receive,
        'sgnt':sgnt_receive,
        'tel':tel_receive
    }
    db.travel.insert_one(doc)

    return jsonify({'result':'success','msg': '행복한 시간 되시기를 바랍니다.'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    data = list(db.travel.find({}, {'_id': False}))
    return jsonify({'client_data':data})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)