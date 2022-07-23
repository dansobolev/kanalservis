from flask import Flask

from config import Config
from views import mod


def create_app() -> Flask:
    flask_app = Flask(__name__)
    flask_app.register_blueprint(mod)
    return flask_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=Config.DEBUG, host=Config.FLASK_HOST, port=Config.FLASK_PORT)
