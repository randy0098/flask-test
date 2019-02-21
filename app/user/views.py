from app.api.authentication import auth
from . import user

@user.route('/', methods=['GET'])
@auth.login_required
def index():
    return 'hi，user!'