# 3rd party libs
import pytest
from flask import abort
from unittest.mock import MagicMock
from werkzeug.exceptions import InternalServerError


@pytest.mark.usefixtures('app_client')
class TestMainApp(object):

    def test_root_endpoint(self):
        response = self.client.get('/invalid')
        assert response.status_code == 404
        assert response.json == "Endpoint /invalid is not found. Please use the available APIs."

    def test_non_existing_endpoint(self):
        response = self.client.get('/wrong/endpoint')
        assert response.status_code == 404
        assert response.json == "Endpoint /wrong/endpoint is not found. Please use the available APIs."

    def test_500_error_code(self):
        response = self.client.get('/error')
        assert response.status_code == 500
        assert response.json == "Internal Server Error."
