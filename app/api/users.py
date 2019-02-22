from flask import jsonify, request, current_app, url_for
from . import api
from ..models import User


@api.route('/users/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())

@api.route('/users')
def get_users():
    users = User.query.all()
    return jsonify({
        'items': [user.to_json() for user in users]
    })

@api.route('/users/pages')
def get_users_page():
    page = request.args.get('page', 1, type=int)
    pagination = User.query.paginate(
        page, per_page=current_app.config['USERS_PER_PAGE'],
        error_out=False)
    users = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_users_page', page=page-1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_users_page', page=page+1)
    return jsonify({
        'users': [user.to_json() for user in users],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })

