import pytest


@pytest.mark.usefixtures('app_client')
class TestFibonacciAPI(object):
    """ Test Class to test Fibonacci API function with different input values and methods."""

    FIBONACCI_API_ENDPOINT = "/fibonacci"

    def test_fibonacci_api(self):
        """ Test to check if Fibonacci API returns 200 code for valid input. """
        response = self.client.get(self.FIBONACCI_API_ENDPOINT+"/4")
        assert response.status_code == 200
        assert response.json == 2

        response = self.client.get(self.FIBONACCI_API_ENDPOINT+"/9")
        assert response.status_code == 200
        assert response.json == 21

    def test_fibonacci_api_with_string_input(self):
        """ Test to check if Fibonacci API returns 400 code for invalid string input. """
        response = self.client.get(self.FIBONACCI_API_ENDPOINT+"/'4'")
        assert response.status_code == 400
        assert response.json == "Input number must be a non-negative integer. Provide a valid input."

    def test_fibonacci_api_with_negative_integer_input(self):
        """ Test to check if Fibonacci API returns 400 code for invalid negative integer input. """
        response = self.client.get(self.FIBONACCI_API_ENDPOINT+"/-4")
        assert response.status_code == 400
        assert response.json == "Input number must be a non-negative integer. Provide a valid input."

    def test_fibonacci_api_with_float_input(self):
        """ Test to check if Fibonacci API returns 400 code for invalid float input. """
        response = self.client.get(self.FIBONACCI_API_ENDPOINT+"/4.1")
        assert response.status_code == 400
        assert response.json == "Input number must be a non-negative integer. Provide a valid input."

    def test_fibonacci_api_with_post(self):
        """ Test to check if Fibonacci API returns 405 code for invalid HTTP method. """
        response = self.client.post(self.FIBONACCI_API_ENDPOINT+"/4")
        assert response.status_code == 405
        assert response.json == "POST method is not allowed. Please use only GET http method."

    def test_fibonacci_api_with_large_input(self):
        """ Test to check if Fibonacci API returns 413 code for a large input than max allowed. """
        response = self.client.get(self.FIBONACCI_API_ENDPOINT+"/200001")
        assert response.status_code == 413
        assert response.json == "Input value 200001 is too large and must be below 200000"
