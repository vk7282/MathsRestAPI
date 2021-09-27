# inbuilt libs
from unittest.mock import MagicMock

# 3rd party libs
import pytest
import flask_monitoringdashboard as dashboard
from werkzeug.exceptions import InternalServerError

# project libs
from app import create_app


def error():
    """ Method to raise internal server error. """
    raise InternalServerError()


@pytest.fixture(scope='class')
def app_client(request):
    """Fixture for creating a test client and attaching to class instance."""
    # mock the dashboard bind call to not multi-thread as it's not needed in testing
    dashboard.bind = MagicMock(return_value=None)
    app = create_app()
    # create an endpoint for testing internal server handling
    app.add_url_rule('/error', 'error', error)

    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            request.cls.client = client
