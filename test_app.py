import unittest

from app import app


class TestDevOpsWebsite(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_homepage_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"DevOps Demo", response.data)

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "healthy")

    def test_about_endpoint(self):
        response = self.client.get("/about")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["project"], "DevOps Demo Website")


if __name__ == "__main__":
    unittest.main(verbosity=2)
