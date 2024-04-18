from flask import Flask
from flask import request

#Library to create api
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello arjun</h1>'

@app.route("/first")
def hello_world1():
    return '<h1>Hello arjun1</h1>'

@app.route("/second")
def hello_world2():
    return '<h1>Hello arjun2</h1>'

@app.route('/test')
def test():
    a=12+90
    return "Kesa hia bhai {}".format(a)

@app.route('/test2')
def test2():
    data = request.args.get('x')
    return 'the value of data {}'.format(data)


if __name__=='__main__':
    app.run(host='0.0.0.0')