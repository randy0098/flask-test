from flask import request, jsonify
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr.db import get_db
from flaskr.model.User import getDb, User

# @app.route('/api/auth')
# def auth():
#     json_data = request.get_json()
#     email = json_data['email']
#     password = json_data['password']
#     return jsonify(token=generate_token(email, password))
#
# with app.test_client() as c:
#     rv = c.post('/api/auth', json={
#         'username': 'flask', 'password': 'secret'
#     })
#     json_data = rv.get_json()
#     assert verify_token(email, json_data['token'])

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/getUsers')
def getUsers():
    db = get_db()
    users = db.execute(
        'select * from user'
    ).fetchall()

    return jsonify(result="success")

@bp.route('/test')
def test():
    # 创建session对象:
    session = getDb()
    # 创建新User对象:
    new_user = User(id=5, name='Bob')
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

    return jsonify(result="success2")
