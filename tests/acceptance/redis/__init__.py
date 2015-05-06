from django.test import Client, SimpleTestCase

from redis import StrictRedis


class RedisTestCase(SimpleTestCase):

    indices = {
        'my-app:ed54cda': '<html><head><meta name="my-app/config/environment" content="%7B%22baseURL%22%3A%22/%22%7D"></head><body><h1>my-app</h1><h2>ed54cda</h2></body></html>',
        'my-app:d696248': '<html><head><meta name="my-app/config/environment" content="%7B%22baseURL%22%3A%22/%22%7D"></head><body><h1>my-app</h1><h2>d696248</h2></body></html>',
        'my-app:7fabf72': '<html><head><meta name="my-app/config/environment" content="%7B%22baseURL%22%3A%22/%22%7D"></head><body><h1>my-app</h1><h2>7fabf72</h2></body></html>',
        'my-app:current': '<html><head><meta name="my-app/config/environment" content="%7B%22baseURL%22%3A%22/%22%7D"></head><body><h1>my-app</h1><h2>7fabf72</h2></body></html>',
        'other-app:fd54cda': '<html><head><meta name="other-app/config/environment" content="%7B%22baseURL%22%3A%22/other-app/%22%7D"></head><body><h1>other-app</h1><h2>fd54cda</h2></body></html>',
        'other-app:e696248': '<html><head><meta name="other-app/config/environment" content="%7B%22baseURL%22%3A%22/other-app/%22%7D"></head><body><h1>other-app</h1><h2>e696248</h2></body></html>',
        'other-app:8fabf72': '<html><head><meta name="other-app/config/environment" content="%7B%22baseURL%22%3A%22/other-app/%22%7D"></head><body><h1>other-app</h1><h2>8fabf72</h2></body></html>',
        'other-app:current': '<html><head><meta name="other-app/config/environment" content="%7B%22baseURL%22%3A%22/other-app/%22%7D"></head><body><h1>other-app</h1><h2>8fabf72</h2></body></html>'
    }

    def setUp(self):
        self.client = Client()
        self.redis = StrictRedis()

        for key, value in self.indices.items():
            self.redis.set(key, value)

    def tearDown(self):
        self.redis.delete(*self.indices.keys())
