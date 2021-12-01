from flask import Flask
import redis
from rq import Queue
import psycopg2
import dataset
from sqlalchemy.sql.schema import Table

app=Flask(__name__)

    
db = dataset.connect('postgresql://postgres:12341234@localhost:5432/sampledb')
table = db['newtable2']
table.insert(dict(count = 200))


r = redis.Redis()
q = Queue(connection=r)
from app import views
from app import tasks

    
   




