from django.test import Client, SimpleTestCase


class GetIndexTestCase(SimpleTestCase):

    def setUp(self):
        self.client = Client()

    def test_should_get_current_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
        self.assertTrue('7fabf72' in response.content.decode('utf-8'))

        response = self.client.get('/abc/def')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
        self.assertTrue('7fabf72' in response.content.decode('utf-8'))

    def test_should_get_specific_index(self):
        response = self.client.get('/r/d696248')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
        self.assertTrue('d696248' in response.content.decode('utf-8'))

        response = self.client.get('/r/d696248/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
        self.assertTrue('d696248' in response.content.decode('utf-8'))

        response = self.client.get('/r/d696248/abc/def')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
        self.assertTrue('d696248' in response.content.decode('utf-8'))

    def test_should_get_not_found_for_non_existing_index(self):
        response = self.client.get('/r/aaaaaa')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')

        response = self.client.get('/r/aaaaaa/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')

        response = self.client.get('/r/aaaaaa/abc/def')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
