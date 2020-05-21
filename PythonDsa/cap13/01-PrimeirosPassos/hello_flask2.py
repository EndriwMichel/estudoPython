# Gerenciar rotas no flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'index !'

@app.route('/hello')
def hello():
    return 'hello word'

@app.route('/members')
def members():
    return 'Members !'

@app.route('/member/<string:name>/')
def get_member(name):
    return name

if __name__ == '__main__':
    app.run()