# 3rd party libs
import pytest


@pytest.mark.usefixtures('app_client')
class TestAckermannAPI(object):
    """ Test Class to test Ackermann API function with different input values and methods."""

    ACKERMANN_API_ENDPOINT = "/ackermann"

    def test_ackermann_api(self):
        """ Test to check if Ackermann API returns 200 code for valid input. """
        response = self.client.get(self.ACKERMANN_API_ENDPOINT+"/1/2")
        assert response.status_code == 200
        assert response.json == 4

    def test_ackermann_api_with_float(self):
        """ Test to check Ackermann API returns 400 code for invalid float input. """
        response = self.client.get(self.ACKERMANN_API_ENDPOINT+"/1.1/2.1")
        assert response.status_code == 400
        assert response.json == "Input number must be a non-negative integer. Provide a valid input."

    def test_ackermann_api_with_string_input(self):
        """ Test to check Ackermann API returns 400 code for invalid string input. """
        response = self.client.get(self.ACKERMANN_API_ENDPOINT+"/'4'/'2'")
        assert response.status_code == 400
        assert response.json == "Input number must be a non-negative integer. Provide a valid input."

    def test_ackermann_api_with_negative_integer_input(self):
        """ Test to check Ackermann API returns 400 code for invalid negative integer input. """
        response = self.client.get(self.ACKERMANN_API_ENDPOINT+"/-1/-4")
        assert response.status_code == 400
        assert response.json == "Input number must be a non-negative integer. Provide a valid input."

    def test_ackermann_api_both_input_as_0(self):
        """ Test to check Ackermann API returns 200 code for both input m & n as 0. """
        response = self.client.get(self.ACKERMANN_API_ENDPOINT+"/0/0")
        assert response.status_code == 200
        assert response.json == 1

    def test_ackermann_api_first_input_as_0(self):
        """ Test to check Ackermann API returns 200 code for input m as 0. """
        response = self.client.get(self.ACKERMANN_API_ENDPOINT+"/0/1")
        assert response.status_code == 200
        assert response.json == 2

    def test_ackermann_api_second_input_as_0(self):
        """ Test to check Ackermann API returns 200 code for input n as 0. """
        response = self.client.get(self.ACKERMANN_API_ENDPOINT+"/1/0")
        assert response.status_code == 200
        assert response.json == 2

    def test_ackermann_api_with_post(self):
        """ Test to check Ackermann API returns 405 in case of invalid HTTP method. """
        response = self.client.post(self.ACKERMANN_API_ENDPOINT+"/4/1")
        assert response.status_code == 405
        assert response.json == "POST method is not allowed. Please use only GET http method."

    def test_ackermann_api_with_large_input(self):
        """ Test to check Ackermann API returns 413 for large input which exceeds the recursion limit. """
        response = self.client.get(self.ACKERMANN_API_ENDPOINT+"/4/2")
        assert response.status_code == 413
        assert response.json == "Input value 4 & 2 is too large for m & n."
