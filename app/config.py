import os


class Config:
    # Secret key for the Flask app
    SECRET_KEY = os.environ.get("SECRET_KEY", "your_secret_key")

    # Database configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Add other configuration variables as needed


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://myuser:mypassword@localhost:5432/mydatabase"
    )


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


# class Localtest(Config):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = (
#         "postgresql://myuser:mypassword@localhost:5432/mydatabasetest"
#     )


class ProductionConfig(Config):
    DEBUG = False


# Dictionary to map environment names to configuration classes
config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
#   "local": Localtest,
}
