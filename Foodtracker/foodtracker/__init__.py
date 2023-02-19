from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models
    # with app.app_context():
    #     db.create_all()

    # Blueprint
    from .main import routes
    app.register_blueprint(routes.bp)

    return app
