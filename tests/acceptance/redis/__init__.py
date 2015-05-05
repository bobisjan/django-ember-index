from django.test import Client, SimpleTestCase

from redis import StrictRedis


class RedisTestCase(SimpleTestCase):

    indices = {
        'my-app:ed54cda': '<html><head><meta name="my-app/config/environment" content="%7B%22baseURL%22%3A%22/%22%7D"></head><body><h1>ed54cda</h1></body></html>',
        'my-app:d696248': '<html><head><meta name="my-app/config/environment" content="%7B%22baseURL%22%3A%22/%22%7D"></head><body><h1>d696248</h1></body></html>',
        'my-app:7fabf72': '<html><head><meta name="my-app/config/environment" content="%7B%22baseURL%22%3A%22/%22%7D"></head><body><h1>7fabf72</h1></body></html>',
        'my-app:current': '<html><head><meta name="my-app/config/environment" content="%7B%22baseURL%22%3A%22/%22%7D"></head><body><h1>7fabf72</h1></body></html>'
    }

    def setUp(self):
        self.client = Client()
        self.redis = StrictRedis()

        for key, value in self.indices.items():
            self.redis.set(key, value)

    def tearDown(self):
        self.redis.delete(*self.indices.keys())
