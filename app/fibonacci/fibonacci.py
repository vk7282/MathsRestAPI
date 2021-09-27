""" Implements the fibonacci series algorithm """


def calculate_fibonacci(number):
    """
    Calculate the number(nth) value of fibonacci series.
    :param number: a non-negative integer
    :return: nth value from the fibonacci series
    """
    if number <= 0:
        return "Number should be a non negative integer."
    fib_series = [0, 1]
    if number > 2:
        for i in range(2, number):
            fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series[number-1]
