from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.routes.crime import crime
    app.register_blueprint(crime)

    return app