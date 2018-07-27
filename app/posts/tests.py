from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase


class PostListTest(APITestCase):
    URL = '/api/posts/'

    def test_post_list_status_code(self):
        response = self.client.get(self.URL)

        pass
        # self.assertEqual(response.)
