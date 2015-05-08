from redis import Redis


class RedisAdapter(object):
    '''An adapter for Redis key-value store.

    Attributes:
        redis (redis.Redis): An instance of a `Redis` class.

    '''

    def __init__(self, **kwargs):
        '''Initialize instance of a `Redis` class.

        Keyword arguments:
            **kwargs: All keyword arguments are passed to the `Redis` object initialization.

        '''
        self.redis = Redis(**kwargs)

    def index_for(self, key):
        '''Fetch index for key from Redis store.

        Keyword arguments:
            key (string): A key for in store lookup.

        Returns:
            An index as string or None if it does not exist.

        '''
        index = self.redis.get(key)

        if index is None:
            return index
        return index.decode('utf-8')
