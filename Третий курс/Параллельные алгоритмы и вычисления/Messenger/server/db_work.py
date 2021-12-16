from peewee import *
import datetime

__all__ = (
    'User',
    'Message',
    'start_session',
)

db = SqliteDatabase('db.sqlite')


def start_session():
    db.connect()
    db.create_tables([User, Message])
    return db


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    session = CharField(null=True)


class Message(BaseModel):
    from_user = ForeignKeyField(User, backref='send')
    to_user = ForeignKeyField(User, backref='recv')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
