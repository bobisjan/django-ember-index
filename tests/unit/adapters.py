import inspect
from unittest import TestCase

from ember_index.adapters import RedisAdapter


class AdaptersTestCase(TestCase):

    def test_should_export_redis_adapter(self):
        self.assertTrue(inspect.isclass(RedisAdapter))
