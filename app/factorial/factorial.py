""" Implements the factorial function algorithm """


def calculate_factorial(number):
    """
    Calculate the factorial of the given number.
    :param number: a non-negative integer of which factorial need to be calculated
    :return fact: the factorial of the provided number
    """
    if number < 0:
        fact = 0
    elif number == 0 or number == 1:
        fact = 1
    else:
        fact = 1
        for i in range(1, number + 1):
            fact = fact*i
    return fact
