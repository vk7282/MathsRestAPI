""" Implements Ackermann function algorithm """

# inbuilt libs
import logging
import sys

logger = logging.getLogger(__name__)

# variable to store the number of recursive calls made
recursion_count = 0


def ackermann_function(m, n):
    """
    Calculate the value of Ackermann function A(m, n).
    According to definition, The Ackermann Function can be explained as below:

               |  n + 1               if m = 0
               |
    A(m,n) =   |  A(m-1, 1)           if m > 0 and n = 0
               |
               |  A(m-1, A(m, n-1))   if m > 0 and n > 0

    :param m: a non-negative integer
    :param n: a non-negative integer
    :return value: the value of the function
    """
    global recursion_count
    try:
        if m < 0 or n < 0:
            raise ValueError("Numbers should be a non negative integer.")
        if m == 0:
            value = n + 1
        elif n == 0:
            recursion_count += 1
            value = ackermann_function(m-1, 1)
        else:
            n1 = ackermann_function(m, n-1)
            recursion_count += 1
            value = ackermann_function(m-1, n1)
        return value
    except RecursionError:
        # we know this exception will be raised considering the heavy recursive calls for even small numbers like A(4,3)
        # and want to gracefully exit from the exception otherwise it will follow up in recursive exception
        logger.exception("Maximum recursion depth reached. Please try with lesser value for m and n.")
        logger.info(f"Total recursive call made before coming to exception is {recursion_count}")
        # Exit gracefully without throwing recursive exception
        sys.exit()
