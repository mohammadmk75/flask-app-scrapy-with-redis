from flask import Flask
import redis
from rq import Queue
from flask_sqlalchemy import SQLAlchemy


app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12341234@localhost/sampledb'
db = SQLAlchemy(app)

class sampledb(db.Model):
    __tablename__ = 'sampledb'

    id = db.Column(db.Integer , primary_key = True)
    url = db.Column(db.String())

    def __init__(self , url):
        self.url = url
    def __repr__(self):
        return '<id {}>'.format(self.id)

r = redis.Redis()
q = Queue(connection=r)
from app import views
from app import tasks


