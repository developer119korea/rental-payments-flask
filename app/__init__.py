from flask import Flask

from app.database import db, ma

from .config import Config
from .core.use_cases import create_use_cases


def create_app(config_name=None):
    app = Flask(__name__)

    if config_name == 'testing':
        app.config.from_object('app.config.TestingConfig')
    else:
        app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    create_rental_use_case, get_rentals_use_case, get_rental_by_key_use_case = create_use_cases()

    from .adapters.web import register_blueprints
    register_blueprints(app, create_rental_use_case, get_rentals_use_case, get_rental_by_key_use_case)

    return app

app = create_app()
