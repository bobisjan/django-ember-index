import re

from . import RedisTestCase


class GetIndexTestCase(RedisTestCase):

    csrf_pattern = re.compile(r'<meta name="X-CSRFToken" content="\w{32}">')

    manifests = {
        'my-app': {
            'base_url': '/',
            'base_tag': False
        },
        'other-app': {
            'base_url': '/other/',
            'base_tag': True
        }
    }

    def test_should_get_current_index(self):
        self.assertGet('/', 'my-app', '7fabf72', True)
        self.assertGet('/abc/def', 'my-app', '7fabf72', True)
        self.assertGet('/#/abc/def', 'my-app', '7fabf72', True)

        self.assertGet('/other/', 'other-app', '8fabf72', True)
        self.assertGet('/other/abc/def', 'other-app', '8fabf72', True)
        self.assertGet('/other/#/abc/def', 'other-app', '8fabf72', True)

    def test_should_get_specific_index(self):
        self.assertGet('/r/d696248/', 'my-app', 'd696248')
        self.assertGet('/r/d696248/abc/def', 'my-app', 'd696248')
        self.assertGet('/r/d696248/#/abc/def', 'my-app', 'd696248')

        self.assertGet('/other/r/e696248/', 'other-app', 'e696248')
        self.assertGet('/other/r/e696248/abc/def', 'other-app', 'e696248')
        self.assertGet('/other/r/e696248/#/abc/def', 'other-app', 'e696248')

    def test_should_get_not_found_for_non_existing_index(self):
        self.assertNotFound('/r/aaaaaa/')
        self.assertNotFound('/r/aaaaaa/abc/def')
        self.assertNotFound('/r/aaaaaa/#/abc/def')

        self.assertNotFound('/other/r/aaaaaa/')
        self.assertNotFound('/other/r/aaaaaa/abc/def')
        self.assertNotFound('/other/r/aaaaaa/#/abc/def')

    def test_should_redirect_to_current_index(self):
        self.assertRedirect('/r/current/', 'my-app')
        self.assertRedirect('/r/current/abc/def', 'my-app')
        self.assertRedirect('/r/current/#abc/def', 'my-app')

        self.assertRedirect('/other/r/current/', 'other-app')
        self.assertRedirect('/other/r/current/abc/def', 'other-app')
        self.assertRedirect('/other/r/current/#/abc/def', 'other-app')

    def test_should_get_without_csrf_token(self):
        with self.settings(MIDDLEWARE_CLASSES=[]):
            self.assertGet('/r/d696248/', 'my-app', 'd696248', csrf=False)
            self.assertGet('/r/d696248/abc/def', 'my-app', 'd696248', csrf=False)
            self.assertGet('/r/d696248/#/abc/def', 'my-app', 'd696248', csrf=False)

            self.assertGet('/other/r/e696248/', 'other-app', 'e696248', csrf=False)
            self.assertGet('/other/r/e696248/abc/def', 'other-app', 'e696248', csrf=False)
            self.assertGet('/other/r/e696248/#/abc/def', 'other-app', 'e696248', csrf=False)

    def assertGet(self, url, manifest, revision, current=False, csrf=True):
        response = self.client.get(url)
        content = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')

        body = '<h1>{0}</h1><h2>{1}</h2>'.format(manifest, revision)
        self.assertTrue(body in content)

        manifest = self.manifests[manifest]
        self.assertBaseUrlInBaseTag(manifest, revision, content, current)
        self.assertBaseUrlInMetaTag(manifest, revision, content, current)
        self.assertCsrfTokenInMetaTag(content, csrf)

    def assertBaseUrlInBaseTag(self, manifest, revision, content, current):
        if not manifest['base_tag']:
            return

        base_tag = None

        if current:
            template = '<base href="{0}" />'
            base_tag = template.format(manifest['base_url'])
        else:
            template = '<base href="{0}r/{1}/" />'
            base_tag = template.format(manifest['base_url'], revision)

        self.assertTrue(base_tag in content)

    def assertBaseUrlInMetaTag(self, manifest, revision, content, current):
        base_url = None

        if current:
            template = '%7B%22baseURL%22%3A%22{0}%22%7D'
            base_url = template.format(manifest['base_url'])
        else:
            template = '%7B%22baseURL%22%3A%22{0}r/{1}/%22%7D'
            base_url = template.format(manifest['base_url'], revision)

        self.assertTrue(base_url in content)

    def assertCsrfTokenInMetaTag(self, content, required=True):
        match = self.csrf_pattern.search(content)
        self.assertEqual(required, bool(match))

    def assertRedirect(self, url, manifest):
        response = self.client.get(url)

        manifest = self.manifests[manifest]
        location = 'http://testserver{0}'.format(manifest['base_url'])

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], location)

    def assertNotFound(self, url):
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
