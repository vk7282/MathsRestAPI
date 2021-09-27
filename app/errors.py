# Module for handling different HTTP Error Codes and returning custom messages.

# inbuilt libs
import logging
# 3rd party libs
from flask import Blueprint, jsonify, request

# create the blueprint for handling errors for status codes 404 and 500.
http_errors = Blueprint('errors', __name__)
logger = logging.getLogger(__name__)


@http_errors.app_errorhandler(404)
def page_not_found(error):
    """
    Handle the cases when the resource URL was not found due to invalid endpoint path.
    :param error: Error object
    :return: Customized JSON error response
    """
    endpoint = request.path
    error_message = f"Endpoint {endpoint} is not found. Please use the available APIs."
    logger.error(f"{error.code}: {error_message}")
    return jsonify(error_message), error.code


@http_errors.app_errorhandler(400)
def invalid_input_data(error):
    """
    Handle the cases when request is aborted due to invalid input.
    :param error: Error object
    :return: Customized JSON error response
    """
    error_message = "Input number must be a non-negative integer. Provide a valid input."
    logger.error(f"{error.code}: {error_message}")
    return jsonify(error_message), error.code


@http_errors.app_errorhandler(405)
def page_not_found(error):
    """
    Handle the cases when the resource URL was not found due to invalid input.
    :param error: Error object
    :return: Customized JSON error response
    """
    error_message = f"{request.method} method is not allowed. Please use only GET http method."
    logger.error(f"{error.code}: {error_message}")
    return jsonify(error_message), error.code


@http_errors.app_errorhandler(500)
def internal_server_error(error):
    """
    Handle the cases when the resource URL throws internal server error.
    :param error: Error object
    :return: Customized JSON error response
    """
    error_message = "Internal Server Error."
    logger.error(f"{error.code}: {error_message}")
    return jsonify(error_message), error.code
