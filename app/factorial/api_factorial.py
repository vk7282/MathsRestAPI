"""
Contains the API implementation for getting the factorial of the number.
To calculate call the below REST API

Request - `curl -X GET http://localhost:5000/factorial/5`
Response - Factorial of the 5 is 120.
"""

# inbuilt libs
import logging
import time

# 3rd party libs
from flask import Blueprint, jsonify, abort

# project libs
from .factorial import calculate_factorial


# create the blueprint API for mathematical function factorial with an endpoint `/factorial`
factorial_api = Blueprint('FactorialAPI', __name__, url_prefix='/factorial')
# get module logger
logger = logging.getLogger(__name__)
# Maximum number which is acceptable from the API for fibonacci series
MAX_NUMBER = 200000


@factorial_api.route("/<int:number>", methods=["GET"])
def get_factorial_value(number):
    """
    Get API call for the factorial function
    :param number: non negative integer number
    :return: JSON response having factorial value with the status code
    """
    try:
        # if input number is greater than MAX_NUMBER raise ValueError to reduce the complexity
        if number > MAX_NUMBER:
            raise ValueError()
        st = time.perf_counter()
        value = calculate_factorial(number)
        et = time.perf_counter()
        logger.info(f"Time to calculate the factorial of {number} is {(et - st)*1000:.4f} ms")
        response = jsonify(value), 200
    except ValueError:
        response = jsonify(f"Input value {number} is too large and must be below {MAX_NUMBER}"), 413
    return response


@factorial_api.route("/<invalid_input>")
def invalid_input_path(invalid_input):
    """
    API call with invalid input for Factorial function
    :param invalid_input: Invalid input i.e string or negative number
    :return: Invalid Input message with 400 status code
    """
    logger.warning(f"Received invalid input {invalid_input} for factorial function.")
    # abort the request and will be handled by the handler in errors
    abort(400)
