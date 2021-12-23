from flask import Flask
import os


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app.secret_key = os.urandom(25)

    with app.app_context():
        from routes import content, errors

        app.register_blueprint(content.content_)
        app.register_blueprint(errors.errors_)

        return app
