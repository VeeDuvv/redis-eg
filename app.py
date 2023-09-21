from flask import Flask, request, jsonify
from redis import Redis
from rq import Queue
from tasks import background_task  # Change is here

app = Flask(__name__)
app.config['REDIS_URL'] = "redis://localhost:6379/0"
redis = Redis.from_url(app.config['REDIS_URL'])
q = Queue('default', connection=redis)

@app.route('/task', methods=['POST'])
def add_task():
    data = request.get_json()
    task_name = data.get('name')
    job = q.enqueue(background_task, task_name)
    return jsonify
