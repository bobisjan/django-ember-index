from . import RedisTestCase


class HeadIndexTestCase(RedisTestCase):

    def test_should_head_current_index(self):
        self.assertHead('/', 200)

    def test_should_head_specific_index(self):
        self.assertHead('/r/d696248', 200)

    def test_should_head_not_found_for_non_existing_index(self):
        self.assertHead('/r/aaaaaa', 404)

    def assertHead(self, url, status_code):
        response = self.client.head(url)
        self.assertEqual(response.status_code, status_code)
        self.assertFalse(response.content)
