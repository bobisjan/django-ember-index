from django.test import Client, SimpleTestCase


class HeadIndexTestCase(SimpleTestCase):

    def setUp(self):
        self.client = Client()

    def test_should_head_current_index(self):
        response = self.client.head('/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.content)

    def test_should_head_specific_index(self):
        response = self.client.head('/r/d696248')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.content)

    def test_should_head_not_found_for_non_existing_index(self):
        response = self.client.head('/r/aaaaaa')
        self.assertEqual(response.status_code, 404)
        self.assertFalse(response.content)
