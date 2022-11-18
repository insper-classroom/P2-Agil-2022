from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from pathlib import Path

from model.db import db
from resources.lms_rotas import Professor, Aluno, Enunciado, ListaEnunciados, ListaProfessores, ListaAlunos, ListaTarefas, Tarefa, AvaliacaoTarefa, SubmissaoTarefa

# Resistente a sistema operacional
FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]
# caminho para a base
rel_arquivo_db = Path('model/agil_lms.db')
caminho_arq_db = src_folder / rel_arquivo_db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{caminho_arq_db.resolve()}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/")
def hello_world():
    return f"<p>Hello, World!</p>"

api.add_resource(ListaProfessores, '/professores')
api.add_resource(Professor, '/professor/<int:id>', '/professor')
api.add_resource(ListaEnunciados, '/enunciado')
api.add_resource(Enunciado, '/professor/<int:id_professor>/enunciado', '/professor/<int:id_professor>/enunciado/<int:id_enunciado>')
api.add_resource(ListaAlunos,'/alunos')
api.add_resource(Aluno, '/aluno/<int:id>', '/aluno')
# Rotas a serem implementadas
api.add_resource(AvaliacaoTarefa, '/professor/<int:id_professor>/enunciado/<int:id_enunciado>/tarefa/<int:id_tarefa>/avaliacao')
api.add_resource(ListaTarefas, '/enunciado/<int:id_enunciado>/tarefa')
api.add_resource(Tarefa, '/aluno/<int:id_aluno>/enunciado/<int:id_enunciado>/tarefa/<int:id_tarefa>', '/aluno/<int:id_aluno>/enunciado/<int:id_enunciado>/tarefa', endpoint='tarefa')
api.add_resource(SubmissaoTarefa, '/aluno/<int:id_aluno>/enunciado/<int:id_enunciado>/tarefa/<int:id_tarefa>/submissao')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)