from flask import request, jsonify
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr.db import get_db

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
