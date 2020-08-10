""" Configurations for FLASK app. """


class Config(object):
    DEBUG = True
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
    DEVELOPMENT = True
    ERROR_404_HELP = False
