"""
Contains the API implementation for getting the nth fibonacci series number.
To get the number call the below REST API

Request - `curl -X GET http://localhost:5000/fibonacci/5`
Response - 5th value in the fibonacci series is 3.
"""

# inbuilt libs
import logging
import time

# 3rd party libs
from flask import Blueprint, jsonify, abort

# project libs
from .fibonacci import calculate_fibonacci


# create the blueprint API for mathematical function factorial with an endpoint `/factorial`
fibonacci_api = Blueprint('FibonacciAPI', __name__, url_prefix='/fibonacci')
# get module logger
logger = logging.getLogger(__name__)
# Maximum number which is acceptable from the API for fibonacci series
MAX_NUMBER = 200000


@fibonacci_api.route("/<int:number>", methods=["GET"])
def get_fibonacci_value(number):
    """
    API call for the factorial function
    :param number: non negative integer number
    :return: JSON response having factorial value with the status code
    """
    try:
        # if input number is greater than MAX_NUMBER raise ValueError to reduce the complexity
        if number > MAX_NUMBER:
            raise ValueError()
        logger.debug("Calling Fibonacci function")
        st = time.perf_counter()
        value = calculate_fibonacci(number)
        et = time.perf_counter()
        logger.info(f"Time to get {number}th value in fibonacci series is {(et - st)*1000:.4f} ms")
        response = jsonify(value), 200
    except ValueError:
        response = jsonify(f"Input value {number} is too large and must be below {MAX_NUMBER}"), 413
    return response


@fibonacci_api.route("/<invalid_input>")
def invalid_input_path(invalid_input):
    """
    API call with invalid input for Fibonacci function
    :param invalid_input: Invalid input i.e string or negative number
    :return: Invalid Input message with 400 status code
    """
    logger.warning(f"Received invalid input {invalid_input} for getting fibonacci series.")
    # abort the request and will be handled by the handler in errors
    abort(400)

