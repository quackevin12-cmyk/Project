print("1.__name__ = " + __name__)
from flask import Flask, request
from markupsafe import escape
from flask import url_for

print("2.__name__ = " + __name__)

app = Flask(__name__)
print("3.app.name = " + app.name)

@app.route('/')
def index():
    return 'index'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do_the_login()'
    else:
        return 'show_the_login_form()'

@app.route("/hi")
def hi():
    name = request.args.get("name", "Flask")
    return f"Hi, {escape(name)}!"

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return f'{username}\'s profile'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == "__main__":
    print("here")
    app.run(debug=True)