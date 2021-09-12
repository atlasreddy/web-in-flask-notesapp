from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "This is a secret key"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    from .views import views
    from .auth import auths
    from .models import User

    create_database(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auths, url_prefix='/auth')

    loginmanager = LoginManager()

    loginmanager.init_app(app)
    # loginmanager.login_view('auths.login_view')

    @loginmanager.user_loader
    def load_user(id):
        print(">="*20, id)
        return User.query.get(int(id))

    return app


def create_database(app):
    if not os.path.exists(f"website/{DB_NAME}"):
        db.create_all(app=app)
        print("database created!")
