from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException


db = SQLAlchemy()


def create_app():
    from .views import main_blueprint, auth_blueprint

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_bloh.db"

    # Setup extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    @app.errorhandler(HTTPException)
    def handle_http_error(exc):
        return render_template("error.html", error=exc), exc.code

    return app
