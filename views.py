from flask import Blueprint


mod = Blueprint('stats', __name__, url_prefix='/api/stats')


@mod.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
