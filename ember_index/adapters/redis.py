from redis import Redis


class RedisAdapter(object):

    def __init__(self, **kwargs):
        self.redis = Redis(**kwargs)

    def index_for(self, key):
        return self.redis.get(key)
