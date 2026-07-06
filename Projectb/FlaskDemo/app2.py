print("1.__name__ = " + __name__)

from flask import render_template
from flask import Flask, request

print("2.__name__ = " + __name__)

app = Flask(__name__)
print("3.app.name = " + app.name)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('test.html', person=name)