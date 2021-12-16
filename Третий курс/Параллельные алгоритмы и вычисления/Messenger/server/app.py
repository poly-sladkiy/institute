import time

import peewee
import sqlite3
from flask import Flask, jsonify, request

from db_work import *
from utils import conf_password, check_user_agent

app = Flask(__name__)


@app.route('/')
async def hello_world():  # put application's code here
    return '<h1>Welcome to XMessenger!</h1>'


@app.route('/register', methods=['GET', 'POST'])
async def register():
    try:
        match request.method:

            case 'GET':
                return '''
                    <form action='' method='post'>
                        <label>Username: <input type="text" name="username"></label>
                        <br>
                        <label>Password: <input type="password" name="password"></label>
                        <input type="submit" value="Register">
                    </form>
                    '''

            case 'POST':

                try:
                    User(
                        username=request.form.get('username'),
                        password=conf_password(request.form.get('password'))
                    ).save()

                except (sqlite3.IntegrityError, peewee.IntegrityError) as er:
                    return jsonify(
                        request='BAD',
                        error=f'Cannot create user - {request.form}',
                        info=str(er),
                    )

                return jsonify(
                    request='OK',
                    error='',
                )

    except Exception as er:
        print(f'[Error]: {er}')
        return jsonify(
            request='BAD',
            error=f'{er}',
        )


@app.route('/login', methods=['POST'])
async def login():

    try:
        await check_user_agent(request)
        username, password = request.form.get('username'), request.form.get('password')

        if User.select()\
                .where(User.username == username)\
                .where(User.password == conf_password(password))\
                .count() > 0:

            return jsonify(
                request='OK',
                error=''
            )

        else:
            return jsonify(
                request='BAD',
                error='Incorrect login or password'
            )

    except Exception as er:
        print(f'[Error]: {er}')


@app.route('/all_users', methods=['GET'])
def all_users():
    data = [i.username for i in User.select(User.username)]

    return jsonify(
        request='OK',
        error='',
        data=str(data)
    )


@app.route('/find_user', methods=['POST'])
def find():
    name = request.form.get('username')
    try:
        data = User.get(User.username == name)

        if data:
            return jsonify(
                request='OK',
                error='',
                username=data.username
            )

    except Exception as er:
        print(f'[Error]: {er}')

        return jsonify(
            request='BAD',
            error='User does not exist',
            username=''
        )


@app.route('/check_messages', methods=['GET'])
def check():
    pass


@app.route('/send_to', methods=['POST'])
def send():
    data = {
        'from_user': request.form.get('from'),
        'to_user': request.form.get('to'),
        'message': request.form.get('msg')
    }

    try:
        Message(
            from_user=request.form.get('from'),
            to_user=request.form.get('to'),
            message=request.form.get('msg')
        ).save()

        return jsonify(
            request='OK',
            error='',
            from_user=data['from_user'],
            to_user=data['to_user'],
        )

    except Exception as er:
        print(f'[Error]: {er}')

        return jsonify(
            request='BAD',
            error='Error sent message',
            from_user=data['from_user'],
            to_user=data['to_user'],
        )


if __name__ == '__main__':
    db = start_session()

    # app.run(debug=True, host='127.0.0.1', port=8080)
    db.close()
