# -*- coding: utf-8 -*-
# from . import views
# from bbsflask.home import views

import pluggy
from .views import bp

hookimpl = pluggy.HookimplMarker('bbsflask')

@hookimpl
def register_blueprint(app):
    print('register blueprint from post')
    app.register_blueprint(bp)