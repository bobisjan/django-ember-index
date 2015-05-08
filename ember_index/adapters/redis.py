from redis import Redis


class RedisAdapter(object):

    def __init__(self, **kwargs):
        self.redis = Redis(**kwargs)

    def index_for(self, key):
        index = self.redis.get(key)

        if index is None:
            return index
        return index.decode('utf-8')
