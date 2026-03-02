from app import db
Cl = db.Column
St = db.String
It = db.Integer
Ft = db.Float

class Jogador(db.Model):
    __tablename__ = "jogadores"

    id = Cl(It, primary_key=True)
    nome = Cl(St(100), nullable=False)
    idade = Cl(It, nullable=False)
    nacao = Cl(St(100))
    altura = Cl(Ft(10,2))
    posicao1 = Cl(St(10))
    posicao2 = Cl(St(10))
    lado_dominate = Cl(St(50))
