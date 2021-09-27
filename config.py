import os
import secrets


class BaseConfig(object):
    """A Base config for the flask app"""
    DEBUG = False
    TESTING = False
    # get the secret key from environment otherwise generate a random hex token.
    SECRET_KEY = os.environ.get("SECRET_KEY", secrets.token_hex(16))
    # One handles incoming requests and other one to perform background operations using the other.
    THREADS_PER_PAGE = 2


class DevelopmentConfig(BaseConfig):
    """Set of configuration for Development environment"""
    # ENV = 'DEVELOPMENT'
    DEBUG = True
    DEVELOPMENT = True


class ProductionConfig(BaseConfig):
    """Set of configuration for Production environment"""
    # ENV = 'PRODUCTION'
    PRODUCTION = True
    DEBUG = False
