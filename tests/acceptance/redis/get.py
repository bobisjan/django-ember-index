from . import RedisTestCase


class GetIndexTestCase(RedisTestCase):

    def test_should_get_current_index(self):
        self.assertGet('/', 200, '7fabf72')
        self.assertGet('/abc/def', 200, '7fabf72')

    def test_should_get_specific_index(self):
        self.assertGet('/r/d696248', 200, 'd696248')
        self.assertGet('/r/d696248/', 200, 'd696248')
        self.assertGet('/r/d696248/abc/def', 200, 'd696248')

    def test_should_get_not_found_for_non_existing_index(self):
        self.assertGet('/r/aaaaaa', 404)
        self.assertGet('/r/aaaaaa/', 404)
        self.assertGet('/r/aaaaaa/abc/def', 404)

    def assertGet(self, url, status_code, content=None):
        response = self.client.get(url)
        self.assertEqual(response.status_code, status_code)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
        if content:
            self.assertTrue(content in response.content.decode('utf-8'))
