from flask import Blueprint, render_template

jogador_bp = Blueprint('jogador', __name__)

@jogador_bp.route("/jogadores")
def lista_jogadores():
    return render_template("jogadores.html")
