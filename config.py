import os


def get_database_url():
    database_url = os.environ.get(
        "DATABASE_URL",
        "sqlite:///jobboard.db",
    )

    if database_url.startswith(
        "postgres://"
    ):
        database_url = database_url.replace(
            "postgres://",
            "postgresql+psycopg://",
            1,
        )

    elif database_url.startswith(
        "postgresql://"
    ):
        database_url = database_url.replace(
            "postgresql://",
            "postgresql+psycopg://",
            1,
        )

    return database_url


class Config:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "development-secret-key",
    )

    SQLALCHEMY_DATABASE_URI = (
        get_database_url()
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAX_CONTENT_LENGTH = (
        2 * 1024 * 1024
    )


class TestingConfig(Config):
    TESTING = True

    SECRET_KEY = "testing-secret-key"

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///:memory:"
    )

    WTF_CSRF_ENABLED = False