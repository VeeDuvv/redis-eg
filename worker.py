import os
from redis import Redis
from rq import Worker, Queue, Connection
from app import app

if __name__ == '__main__':
    redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    conn = Redis.from_url(redis_url)
    with Connection(conn):
        with app.app_context():
            worker = Worker(['default'])
            worker.work()
