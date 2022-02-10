import unittest

from stupy.stupy_api import StupyApi


class TestApiHandler(unittest.TestCase):
    def test_get_success(self):
        response = StupyApi.get()
        assert response == 200

    def test_post_success(self):
        body = '{"body": "ok"}'
        response = StupyApi.post(body)

        assert response == 200

    def test_post_error(self):
        body = '{"body": "error"}'
        response = StupyApi.post(body)

        assert response == 400
