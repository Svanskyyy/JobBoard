from flask import Flask

from config import Config
from app.extensions import (
    db,
    login_manager,
    migrate,
)
from app.logging_config import configure_logging


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(
        config_class
    )

    if not app.config.get("TESTING"):
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