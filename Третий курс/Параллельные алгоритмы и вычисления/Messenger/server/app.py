import time

import peewee
import sqlite3
from flask import Flask, jsonify, request

from db_work import *
from utils import conf_password, check_user_agent

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Welcome to XMessenger!</h1>'


@app.route('/register', methods=['GET', 'POST'])
def register():
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
                    password = conf_password(request.form.get('password'))

                    User(
                        username=request.form.get('username'),
                        password=password
                    ).save()

                except (sqlite3.IntegrityError, peewee.IntegrityError) as er:
                    return jsonify(
                        request='BAD',
                        error=f'Cannot create user - {request.form}',
                        info=str(er),
                    )

                except:
                    print(f'[Error]: /register - {request.form} - {password}')

                    return jsonify(
                        request='BAD',
                        error=f'Unknown error',
                        info='',
                    )

                return jsonify(
                    request='OK',
                    error='',
                )

    except Exception as er:
        print(f'[Error]: /register - {er}')

        return jsonify(
            request='BAD',
            error=str(er),
            username=''
        )

    except:
        print(f'[Error]: /register')

        return jsonify(
            request='BAD',
            error='',
            username=''
        )


@app.route('/login', methods=['POST'])
def login():
    try:
        # check_user_agent(request)

        if User.select() \
                .where(User.username == request.form.get('username')) \
                .where(User.password == conf_password(request.form.get('password'))) \
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
        print(f'[Error]: /login - {er}')

        return jsonify(
            request='BAD',
            error=str(er),
            username=''
        )

    except:
        print(f'[Error]: /login - {username}')

        return jsonify(
            request='BAD',
            error='',
            username=''
        )


@app.route('/find_user', methods=['POST'])
def find():
    try:
        # check_user_agent(request)

        name = request.form.get('username')
        data = User.get(User.username == name)

        if data:
            return jsonify(
                request='OK',
                error='',
                username=data.username
            )

    except Exception as er:
        print(f'[Error]: /find_user - {er}')

        return jsonify(
            request='BAD',
            error=str(er),
            username=''
        )

    except:
        print(f'[Error]: /find_user - {name}')

        return jsonify(
            request='BAD',
            error='',
            username=''
        )


@app.route('/all_msg', methods=['GET'])
def all_messages():
    qs = [i for i in Message.select()]

    return jsonify(
        request='OK',
        error='',
        data=str(qs)
    )


@app.route('/check_messages', methods=['GET'])
def check():
    try:
        # check_user_agent(request)

        qs = Message.select() \
            .where(
            (Message.from_user == request.args.get('username')) |
            (Message.to_user == request.args.get('username'))
        )

        data = []
        for msg in qs:
            data.append(
                {
                    "from": str(msg.from_user_id),
                    "to": str(msg.to_user_id),
                    "msg": str(msg.message),
                    "time": msg.created_date.ctime()
                }
            )

        return jsonify(
            request="OK",
            error="",
            data=data,
        )

    except Exception as er:
        print(f'[Error]: /check_messages - {er}')

        return jsonify(
            request='BAD',
            error=str(er),
            username=''
        )

    except:
        print(f'[Error]: /check_messages')

        return jsonify(
            request='BAD',
            error='',
            username=''
        )


@app.route('/send_to', methods=['POST'])
def send():
    try:
        # check_user_agent(request)

        Message(
            from_user=request.form.get('from'),
            to_user=request.form.get('to'),
            message=request.form.get('msg')
        ).save()

        return jsonify(
            request='OK',
            error='',
            from_user=request.form.get('from'),
            to_user=request.form.get('to'),
        )

    except Exception as er:
        print(f'[Error]: /send_to - {er}')

        return jsonify(
            request='BAD',
            error=str(er),
            username=''
        )

    except:
        print(f'[Error]: /send_to')

        return jsonify(
            request='BAD',
            error='',
            username=''
        )


if __name__ == '__main__':
    db = start_session()

    app.run(debug=False, host='127.0.0.1', port=8080)
    db.close()
