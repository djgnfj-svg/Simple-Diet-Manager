from rest_framework.test import APITestCase

class DietMakeTest(APITestCase):
    def setUp(self) -> None:
        self.url = '/api/week-diets/' 
        return super().setUp()
    
    # 테스트 목표
    # 1. 요청이 정상적으로 들어오면 get은 지원하지 않는다.
    def test_diet_make_get_fail(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)

    # 2. 요청이 정상적으로 들어오면 post는 지원한다.
    # def test_diet_make(self):
    #     response = self.client.post(self.url)
    #     self.assertEqual(response.status_code, 201)

        # 2-1 요청이 정상적으로 들어오면 6일치의 diet가 생성된다.
        