import sys

import pluggy
from flask import Flask

from bbsflask.plugin import spec


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.plugin_manager = pluggy.PluginManager('bbsflask')
    register_bluerpint(app)
    return app


def register_bluerpint(app):
    app.plugin_manager.add_hookspecs(spec)
    for name, module in sys.modules.items():
        if name.startswith('bbsflask'):
            ret = app.plugin_manager.register(module)
    app.plugin_manager.hook.register_blueprint(app=app)