from flask import (
    Blueprint,
    render_template
)


bp = Blueprint('post', __name__, url_prefix='/post')

def index():
    return render_template('post/post.html')


bp.add_url_rule('/', view_func=index)
