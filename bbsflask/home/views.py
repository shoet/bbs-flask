from flask import (
    Blueprint,
    render_template
)



bp = Blueprint('home', __name__, url_prefix='/home')

def index():
    return render_template('home/home.html')


bp.add_url_rule('/', view_func=index)
