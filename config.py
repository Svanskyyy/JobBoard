import os


class Config:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "development-secret-key",
    )

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///jobboard.db",
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAX_CONTENT_LENGTH = 2 * 1024 * 1024


class TestingConfig(Config):
    TESTING = True

    SECRET_KEY = "testing-secret-key"

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///:memory:"
    )

    WTF_CSRF_ENABLED = False