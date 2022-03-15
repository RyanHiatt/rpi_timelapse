import secrets


class Config(object):
    SECRET_KEY = secrets.token_hex()
    DEBUG = True
    ENV = 'development'
