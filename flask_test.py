import os

from flask import render_template, redirect
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Role

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db, User=User, Role=Role)

# @app.cli.command()
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)

# @app.route('/', methods=['GET'])
# def index():
#     return render_template("index.html")

@app.route('/<path:path>', methods=['GET'])
def get_html(path):
    return render_template(path)

@app.route('/')
def index():
    return redirect('/index.html')

if __name__ == '__main__':
    app.run()