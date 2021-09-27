# Module to setup the root logging structure so it can be used across the application.

# inbuilt libs
import logging
import os


def init_logging():
    """
    Initialize the logging for flask application with basic configuration.
    """

    # Get the gunicorn logger so we log details from gunicorn to the same place
    gunicorn_logger = logging.getLogger('gunicorn.error')
    handlers = gunicorn_logger.handlers
    # get the current directory path
    root_dir = os.path.dirname(os.curdir)
    # get the log dir path from environment if exists otherwise take the root dir
    log_dir = os.environ.get("LOG_PATH", root_dir)
    # create the final log directory path if doesn't exist
    log_dir_path = os.path.join(log_dir, 'logs')
    if not os.path.exists(log_dir_path):
        os.mkdir(log_dir_path)
    # create the log file in log directory
    log_file_path = os.path.join(log_dir_path, 'app.log')
    # file handler for the logging
    file_handler = [logging.FileHandler(log_file_path)]
    # extend the handlers with gunicorn handlers
    handlers.extend(file_handler)
    # format of the logging from the application and gunicorn
    formatters = '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)d] %(message)s'
    # Use the log level from environment else use from gunicorn
    log_level = os.environ.get('LOG_LEVEL', gunicorn_logger.level)
    # create a root logging so it can be used in all other modules.
    logging.basicConfig(level=log_level, handlers=handlers, format=formatters, datefmt='%Y-%m-%dT%H:%M:%S')
