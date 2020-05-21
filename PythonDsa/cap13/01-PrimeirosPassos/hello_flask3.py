# Trabalhando com templates no Flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'App Index !'

@app.route('/hello/<string:name>/')
def get_member(name):
    return render_template('template01.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0')