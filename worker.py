# worker.py

import os
from redis import Redis
from rq import Worker, Queue, Connection
from shared import init_app
from flask import Flask

app = Flask(__name__)
q = init_app(app)

if __name__ == "__main__":
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    conn = Redis.from_url(redis_url)
    with Connection(conn):
        with app.app_context():
            worker = Worker(["default"])
            worker.work()
