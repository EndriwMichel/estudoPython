# Aplicação CRUD de exemplo: portifolio do desenvolvedor
from flask import Flask, render_template, flash, redirect, request, session, abort, json
from werkzeug import generate_password_hash, check_password_hash
from business import appDataBase

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSignUp')
def showsignup():
    return render_template('signup.html')

@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # Valida os dados recebidos
        if _name and _email and _password:
            _hashed_password = generate_password_hash(_password)

            appDb = appDataBase().insertUser(_name, _email, _hashed_password)

            if appDb:
                return json.dumps({'message':'User criado com sucesso!'})
            else:
                return json.dumps({'error !'})

        else:
            return json.dumps({'html':'<span>preencha os campos requeridos</span>'})

    except Exception as e:
        return json.dumps({'erro': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
