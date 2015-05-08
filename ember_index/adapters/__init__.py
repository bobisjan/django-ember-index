'''A module with index adapters.

An adapter has to implement `index_for(self, key)` method,
which returns appropriate index as string or None if it does not exist.

'''

from .redis import RedisAdapter


__all__ = ['RedisAdapter']
