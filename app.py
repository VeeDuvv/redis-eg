from flask import Flask, request, render_template, redirect, url_for
from redis import Redis
from rq import Queue
from tasks import background_task
from app_factory import create_app


from flask import Flask, request, render_template, redirect, url_for
from tasks import background_task
from shared import init_app

app = create_app()
q = init_app(app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/task", methods=["POST"])
def add_task():
    if request.is_json:
        task_name = request.get_json().get("name")
    else:
        task_name = request.form["name"]

    task_name = request.form["name"]
    job = q.enqueue(background_task, task_name)
    return redirect(url_for("get_results", job_key=job.id))


@app.route("/results/<job_key>", methods=["GET"])
def get_results(job_key):
    try:
        job = q.fetch_job(job_key)
        if job:
            return render_template(
                "job_status.html", status=job.get_status(), result=job.result
            )
        else:
            return "No such job."
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)
