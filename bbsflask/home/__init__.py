# -*- coding: utf-8 -*-
import pluggy
from .views import bp

hookimpl = pluggy.HookimplMarker('bbsflask')

@hookimpl
def register_blueprint(app):
    print('register blueprint from home')
    app.register_blueprint(bp)