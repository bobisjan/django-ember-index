import inspect
from unittest import TestCase

from ember_index import index, RedisAdapter


class ImportTestCase(TestCase):

    def test_should_export_index(self):
        self.assertTrue(inspect.isfunction(index))

    def test_should_export_redis_adapter(self):
        self.assertTrue(inspect.isclass(RedisAdapter))
