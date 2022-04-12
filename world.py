import os 

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "world hello"

@app.route('/foo')
def foo():
    return "hey there you found foo"

@app.route('/bar')
def bar():
    return "hey there you found bar"

@app.route('/test')
def test():
    return "hey there you found test"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', '5000'))
