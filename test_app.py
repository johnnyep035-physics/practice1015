import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        # 建立 Flask 測試用戶端
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_home_page_status_code(self):
        """測試首頁回應狀態碼是否為 200"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_heading(self):
        """測試首頁是否包含 Hello, World! 標題"""
        response = self.client.get('/')
        self.assertIn('Hello, World!'.encode('utf-8'), response.data)

if __name__ == '__main__':
    unittest.main()
