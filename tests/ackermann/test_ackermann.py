# 3rd party libs
import pytest
# project libs
from app.ackermann import ackermann_function


class TestFibonacci:
    """ Test Class to test Ackermann function with different input values."""

    def test_ackermann_function_with_negative_integer(self):
        """ Test to check if either m or n negative should return validation message. """
        with pytest.raises(ValueError, match="Numbers should be a non negative integer."):
            ackermann_function(-1, 2)

    def test_ackermann_function_with_string(self):
        """ Test to check if the string is passed instead of integers should raise TypeError exception """
        with pytest.raises(TypeError):
            ackermann_function("9", 1)

    def test_ackermann_function_with_m_zero(self):
        """ Test to check if m is zero should return n+1 """
        value = ackermann_function(0, 1)
        assert value == 2

    def test_ackermann_function_with_n_zero(self):
        """ Test to check if n is zero should return A(m-1, 1) """
        value = ackermann_function(1, 0)
        assert value == 2

    def test_ackermann_function_with_m_n_zero(self):
        """ Test to check if both m & n is zero should return n+1 """
        value = ackermann_function(0, 0)
        assert value == 1

    def test_ackermann_function(self):
        """ Test to check if calculated value is expected if both m & n are greater than 0 """
        value = ackermann_function(1, 2)
        assert value == 4

    def test_ackermann_function_recursion_error(self):
        """ Test to check if large values of m & n should raise Recursion error """
        with pytest.raises(SystemExit):
            ackermann_function(4, 2)
