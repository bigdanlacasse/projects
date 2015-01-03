import redis

def setup_redis(host="127.0.0.1"):
    return redis.Redis(host=host)
