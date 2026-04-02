import unittest

from app.main import route


class RouteTests(unittest.TestCase):
    def test_health_endpoint(self) -> None:
        status, body = route("/health")
        self.assertEqual(status, 200)
        self.assertEqual(body, {"status": "ok"})

    def test_root_endpoint(self) -> None:
        status, body = route("/")
        self.assertEqual(status, 200)
        self.assertEqual(body["name"], "SIH25 Service")

    def test_not_found(self) -> None:
        status, body = route("/missing")
        self.assertEqual(status, 404)
        self.assertEqual(body, {"error": "not_found"})


if __name__ == "__main__":
    unittest.main()
