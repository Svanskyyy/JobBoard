import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "development-secret-key")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///jobboard.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False