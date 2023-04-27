import os

from bbsflask.app import create_app
from bbsflask.settings import config

app = create_app(config[os.environ['APP_ENV']])