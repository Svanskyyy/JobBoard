from flask import Flask

from config import Config
from app.extensions import db, migrate, login_manager
from app.logging_config import configure_logging


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    configure_logging(app)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.main.routes import main_bp
    app.register_blueprint(main_bp)

    from app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    from app.jobs.routes import jobs_bp
    app.register_blueprint(jobs_bp)

    from app.errors import errors_bp
    app.register_blueprint(errors_bp)

    from app import models

    return app