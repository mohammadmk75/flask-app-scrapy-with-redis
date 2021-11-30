from app import app
from app import r
from app import q
from app.tasks import count_words
from time import strftime
from flask import render_template, request

@app.route("/add-task", methods=["GET", "POST"])
def task():

    jobs = q.jobs  
    message = None

    if request.args:  

        url = request.args.get("url")  

        task = q.enqueue(count_words, url)  

        jobs = q.jobs  

        q_len = len(q) 

        message = f"Task queued at {task.enqueued_at.strftime('%a, %d %b %Y %H:%M:%S')}. {q_len} jobs queued"


    return render_template("index.html", message=message, jobs=jobs)

