from flask import Blueprint, render_template

jogador_bp = Blueprint('jogador', __name__)

@jogador_bp.route("/")
def index():
    return render_template("index.html")

@jogador_bp.route("/jogadores")
def lista_jogadores():
    return render_template("jogadores.html")
