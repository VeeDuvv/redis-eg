# shared.py
# purpose of this file is to initialize the redis queue

from redis import Redis
from rq import Queue


def init_app(app):
    app.config["REDIS_URL"] = "redis://localhost:6379/0"
    redis = Redis.from_url(app.config["REDIS_URL"])
    q = Queue("default", connection=redis)
    return q
