from flask import Flask, render_template, flash, redirect, request, session, abort

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask app !'

@app.route('/hello/<string:name>/')
def get_member(name):
    return render_template('template02.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')