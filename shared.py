# shared.py

from redis import Redis
from rq import Queue


def init_app(app):
    app.config["REDIS_URL"] = "redis://localhost:6379/0"
    redis = Redis.from_url(app.config["REDIS_URL"])
    q = Queue("default", connection=redis)
    return q
