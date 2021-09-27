# 3rd party libs
import pytest
# project libs
from app.fibonacci import calculate_fibonacci


class TestFibonacci(object):
    """ Test Class to test fibonacci series with different input values."""

    def test_fibonacci_with_negative_integer(self):
        """ Test to check if negative integer input should return validation message. """
        output = calculate_fibonacci(-9)
        assert output == "Number should be a non negative integer."

    def test_fibonacci_with_string(self):
        """ Test to check if string input should raise TypeError exception. """
        with pytest.raises(TypeError):
            calculate_fibonacci("9")

    def test_fibonacci_first_value(self):
        """ Test to check if the first fibonacci series element should be 0. """
        value = calculate_fibonacci(1)
        assert value == 0

    def test_fibonacci(self):
        """ Test to check the fibonacci series should produce expected output. """
        value = calculate_fibonacci(9)
        assert value == 21
