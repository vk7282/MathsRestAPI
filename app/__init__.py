# inbuilt libs
import os
import logging

# 3rd party libs
from flask import Flask
import flask_monitoringdashboard as dashboard

# project libs
from app.logs import init_logging
from config import DevelopmentConfig, ProductionConfig


# get current module logger
logger = logging.getLogger(__name__)


# Create factory method for our Flask application
def create_app():
    """
    A factory method for our dynamic environment flask application which
        * Initializes the logging
        * Bind a monitoring dashboard
        * Registers the blueprint for our mathematical functions
    :return app: application object as an instance of Flask
    """
    app = Flask(__name__)

    # Initialize the logging
    init_logging()

    # Bind the application with dashboard to show the API endpoint stats
    logger.info("Loading the Monitoring Dashboard...")
    dashboard.bind(app, False)
    logger.info("Monitoring Dashboard loaded.")

    # load the proper config environment
    config_obj = ProductionConfig if os.environ.get('PRODUCTION') else DevelopmentConfig
    app.config.from_object(config_obj)

    logger.info('Starting the app')

    # Import a module / component using its blueprint handler variable
    from app.factorial import factorial_api
    from app.ackermann import ackermann_api
    from app.fibonacci import fibonacci_api
    from app.errors import http_errors

    # Register blueprint(s)
    logger.info("Registering blueprints for Mathematical functions")
    app.register_blueprint(factorial_api)
    app.register_blueprint(ackermann_api)
    app.register_blueprint(fibonacci_api)
    app.register_blueprint(http_errors)

    return app
