from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes.jogador_routes import jogador_bp
    app.register_blueprint(jogador_bp)

    return app
