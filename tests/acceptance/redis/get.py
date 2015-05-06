from . import RedisTestCase


class GetIndexTestCase(RedisTestCase):

    base_url = {
        'my-app': '/',
        'other-app': '/other-app/'
    }

    def test_should_get_current_index(self):
        self.assertGet('/', 'my-app', '7fabf72', True)
        self.assertGet('/abc/def', 'my-app', '7fabf72', True)
        self.assertGet('/#/abc/def', 'my-app', '7fabf72', True)

        self.assertGet('/other-app/', 'other-app', '8fabf72', True)
        self.assertGet('/other-app/abc/def', 'other-app', '8fabf72', True)
        self.assertGet('/other-app/#/abc/def', 'other-app', '8fabf72', True)

    def test_should_get_specific_index(self):
        self.assertGet('/r/d696248/', 'my-app', 'd696248')
        self.assertGet('/r/d696248/abc/def', 'my-app', 'd696248')
        self.assertGet('/r/d696248/#/abc/def', 'my-app', 'd696248')

        self.assertGet('/other-app/r/e696248/', 'other-app', 'e696248')
        self.assertGet('/other-app/r/e696248/abc/def', 'other-app', 'e696248')
        self.assertGet('/other-app/r/e696248/#/abc/def', 'other-app', 'e696248')

    def test_should_get_not_found_for_non_existing_index(self):
        self.assertNotFound('/r/aaaaaa/')
        self.assertNotFound('/r/aaaaaa/abc/def')
        self.assertNotFound('/r/aaaaaa/#/abc/def')

        self.assertNotFound('/other-app/r/aaaaaa/')
        self.assertNotFound('/other-app/r/aaaaaa/abc/def')
        self.assertNotFound('/other-app/r/aaaaaa/#/abc/def')

    def test_should_redirect_to_current_index(self):
        self.assertRedirect('/r/current/', 'my-app')
        self.assertRedirect('/r/current/abc/def', 'my-app')
        self.assertRedirect('/r/current/#abc/def', 'my-app')

        self.assertRedirect('/other-app/r/current/', 'other-app')
        self.assertRedirect('/other-app/r/current/abc/def', 'other-app')
        self.assertRedirect('/other-app/r/current/#/abc/def', 'other-app')

    def assertGet(self, url, manifest, revision, current=False):
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')

        body = '<h1>{0}</h1><h2>{1}</h2>'.format(manifest, revision)
        self.assertTrue(body in response.content.decode('utf-8'))

        if current:
            template = '%7B%22baseURL%22%3A%22{0}%22%7D'
            base_url = template.format(self.base_url[manifest])
        else:
            template = '%7B%22baseURL%22%3A%22{0}r/{1}/%22%7D'
            base_url = template.format(self.base_url[manifest], revision)

        self.assertTrue(base_url in response.content.decode('utf-8'))

    def assertRedirect(self, url, manifest):
        response = self.client.get(url)
        location = 'http://testserver{0}'.format(self.base_url[manifest])

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], location)

    def assertNotFound(self, url):
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
