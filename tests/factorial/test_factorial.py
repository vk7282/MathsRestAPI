# 3rd party libs
import pytest
# project libs
from app.factorial import calculate_factorial


class TestFactorial(object):
    """ Test Class to test factorial function with different input values."""

    def test_factorial_with_negative_integer(self):
        """ Test to check if negative integer input should return 0. """
        output = calculate_factorial(-9)
        assert output == 0

    def test_factorial_with_string(self):
        """ Test to check if string input should raise TypeError exception. """
        with pytest.raises(TypeError):
            calculate_factorial("9")

    def test_factorial_with_input_value_0(self):
        """ Test to check if the first fibonacci series element should be 0. """
        value = calculate_factorial(0)
        assert value == 1

    def test_factorial_with_input_value_1(self):
        """ Test to check if the first fibonacci series element should be 0. """
        value = calculate_factorial(1)
        assert value == 1

    def test_factorial(self):
        """ Test to check the fibonacci series should produce expected output. """
        value = calculate_factorial(4)
        assert value == 24
