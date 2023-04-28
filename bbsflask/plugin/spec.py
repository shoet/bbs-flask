import pluggy

hookspec = pluggy.HookspecMarker('bbsflask')

@hookspec
def register_blueprint(app):
    """register_blueprint"""