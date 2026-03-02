from flask import Flask
from app.extension_py import db, mg
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mg.init_app(app, db)

    from .routes.jogador_routes import jogador_bp
    app.register_blueprint(jogador_bp)

    with app.app_context():
        db.create_all()

    return app
