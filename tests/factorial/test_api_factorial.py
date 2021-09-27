# 3rd party libs
import pytest


@pytest.mark.usefixtures('app_client')
class TestFactorialAPI(object):
    """ Test Class to test Factorial API function with different input values and methods."""

    FACTORIAL_API_ENDPOINT = "/factorial"

    def test_factorial_api(self):
        """ Test to check if Factorial API returns 200 code for valid input. """
        response = self.client.get(self.FACTORIAL_API_ENDPOINT+"/4")
        assert response.status_code == 200
        assert response.json == 24

    def test_factorial_api_with_input_0(self):
        """ Test to check if Factorial API returns 200 code for input value 0. """
        response = self.client.get(self.FACTORIAL_API_ENDPOINT+"/0")
        assert response.status_code == 200
        assert response.json == 1

    def test_factorial_api_with_input_1(self):
        """ Test to check if Factorial API returns 200 code for input value 1. """
        response = self.client.get(self.FACTORIAL_API_ENDPOINT+"/1")
        assert response.status_code == 200
        assert response.json == 1

    def test_factorial_api_with_string_input(self):
        """ Test to check if Factorial API returns 400 code for invalid string input. """
        response = self.client.get(self.FACTORIAL_API_ENDPOINT+"/'4'")
        assert response.status_code == 400
        assert response.json == "Input number must be a non-negative integer. Provide a valid input."

    def test_factorial_api_with_negative_integer_input(self):
        """ Test to check if Factorial API returns 400 code for invalid negative integer input. """
        response = self.client.get(self.FACTORIAL_API_ENDPOINT+"/-4")
        assert response.status_code == 400
        assert response.json == "Input number must be a non-negative integer. Provide a valid input."

    def test_factorial_api_with_float_input(self):
        """ Test to check if Factorial API returns 400 code for invalid float input. """
        response = self.client.get(self.FACTORIAL_API_ENDPOINT+"/4.2")
        assert response.status_code == 400
        assert response.json == "Input number must be a non-negative integer. Provide a valid input."

    def test_factorial_api_with_post(self):
        """ Test to check if Factorial API returns 405 code for invalid HTTP method call. """
        response = self.client.post(self.FACTORIAL_API_ENDPOINT+"/4")
        assert response.status_code == 405
        assert response.json == "POST method is not allowed. Please use only GET http method."

    def test_factorial_api_with_large_input(self):
        """ Test to check if Factorial API returns 413 code for a large input than max allowed. """
        response = self.client.get(self.FACTORIAL_API_ENDPOINT+"/200001")
        assert response.status_code == 413
        assert response.json == "Input value 200001 is too large and must be below 200000"
