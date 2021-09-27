"""
Contains the API implementation for calculating the Ackermann Function for m & n.
To calculate call the below REST API

Request - `curl -X GET http://localhost:5000/ackermann/1/2`
Response - Value of A(1, 2) is 4.
"""

# inbuilt libs
import logging
import time
import sys

# 3rd party libs
from flask import Blueprint, jsonify, abort

# project libs
from .ackermann import ackermann_function


# create the blueprint API for mathematical Ackermann function with an endpoint `/ackermann`
ackermann_api = Blueprint('AckermannAPI', __name__, url_prefix='/ackermann')
logger = logging.getLogger(__name__)


@ackermann_api.route("/<int:m>/<int:n>", methods=["GET"])
def get_ackermann_value(m, n):
    """
    API call for the Ackermann function
    :param m: non-negative integer number
    :param n: non-negative integer number
    :return: JSON response having ackermann value with the status code
    """
    logger.debug("Calling ackermann function")
    st = time.perf_counter()
    # Get the recursion limit and save to reset back later
    recursion = sys.getrecursionlimit()
    # set a new recursion limit
    sys.setrecursionlimit(10000)
    try:
        value = ackermann_function(m, n)
        et = time.perf_counter()
        logger.info(f"Time to calculate the value of A({m}, {n}) is {(et - st)*1000:.4f} ms")
        response = jsonify(value), 200
    except SystemExit:
        # Catch systemExit exception, since we call in the actual algorithm implementation.
        logger.exception(f"SystemExit exception raised from Ackermann Function for input values {m} and {n}")
        response = jsonify(f"Input value {m} & {n} is too large for m & n."), 413
        et = time.perf_counter()
        logger.info(f"Time took to process the value of A({m}, {n}) is {(et - st)*1000:.4f} ms")
    # revert back the recursion value to old value in python
    sys.setrecursionlimit(recursion)
    return response


@ackermann_api.route("/<invalid_input_m>/<invalid_input_n>")
def invalid_input_path(invalid_input_m, invalid_input_n):
    """
    API call with invalid input for Ackermann function
    :param invalid_input_m: Invalid input i.e string or negative number
    :param invalid_input_n: Invalid input i.e string or negative number
    :return: Invalid Input message with 400 status code
    """
    logger.warning(f"Received invalid input {invalid_input_m} and {invalid_input_n} for ackermann function.")
    # abort the request and will be handled by the handler in errors
    abort(400)
