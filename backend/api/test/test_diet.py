from rest_framework.test import APITestCase


class DietTest(APITestCase):
    def setUp(self):
        self.url = '/api/diets/'
        return super().setUp()

    def test_diet_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
