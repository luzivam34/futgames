from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import or_

from app import db
from app.models.jogador_model import Jogador

jogador_bp = Blueprint('jogador', __name__)

@jogador_bp.route("/")
def index():
    return render_template("index.html")

@jogador_bp.route("/jogadores")
def lista_jogadores():
    jogadores = Jogador.query.order_by(Jogador.nome).all()
    goleiros = Jogador.query.order_by(Jogador.nome).filter_by(posicao1="GK").all()
    zagueiros = Jogador.query.order_by(Jogador.nome).filter( or_(Jogador.posicao1=="CB",Jogador.posicao2=="CB")).all()
    lateral = Jogador.query.order_by(Jogador.nome).filter(or_(Jogador.posicao1=="SB", Jogador.posicao2=="SB")).all()
    meio_campo_defesivo = Jogador.query.order_by(Jogador.nome).filter(or_(Jogador.posicao1=="DMF", Jogador.posicao2 == "DMF")).all()
    meio_campo_central = Jogador.query.order_by(Jogador.nome).filter(or_(Jogador.posicao1=="CMF", Jogador.posicao2 == "CMF")).all()
    meio_campo_ofensivo = Jogador.query.order_by(Jogador.nome).filter(or_(Jogador.posicao1=="AMF", Jogador.posicao2 == "AMF")).all()
    return render_template(
        "jogadores.html",
        jogadores=jogadores, goleiros=goleiros, zagueiros=zagueiros,
        lateral=lateral, meio_campo_defesivo=meio_campo_defesivo, meio_campo_central=meio_campo_central,
        meio_campo_ofensivo=meio_campo_ofensivo
    )

@jogador_bp.route("/cadastro", methods=['POST', "GET"])
def cadastrar_jogador():
    if request.method == "POST":
        nome = request.form["nome"]
        idade = request.form["idade"]
        altura = request.form["altura"]
        nacao = request.form["nacao"]
        posicao1 = request.form["posicao1"]
        posicao2 = request.form["posicao2"]
        lado_dominate = request.form["lado_dominate"]

        jogador = Jogador(
            nome=nome,
            idade=idade,
            altura=altura,
            nacao=nacao,
            posicao1=posicao1,
            posicao2=posicao2,
            lado_dominate=lado_dominate
        )
        db.session.add(jogador)
        db.session.commit()

        return redirect(url_for("jogador.lista_jogadores"))

    return render_template("cadastrar_jogador.html")
