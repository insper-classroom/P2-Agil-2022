from model.db import db
from datetime import datetime
#from __future__ import annotations
#from model.lms_models import ProfessorModel, AlunoModel, TarefaModel, EnunciadoModel



class ProfessorModel(db.Model):
    __tablename__ = "tbl_professor"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))


    def __init__(self, nome, **kwargs):
        self.nome = nome
        super(ProfessorModel, self).__init__(**kwargs)

    def toDict(self):
        return {'id': self.id, 'nome':self.nome}

    def __repr__(self):
        return f"Professor(id={self.id}, nome={self.nome})"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def criar_enunciado(self, titulo, descricao, data_entrega):
        enunciado = EnunciadoModel(id_professor = self.id, titulo = titulo, descricao= descricao, data_entrega= data_entrega)
        enunciado.save()
        return enunciado

    def deletar_enunciado(self, id_enunciado):
        enunciado = EnunciadoModel.find(id_enunciado)
        if enunciado:
            # verify if enunciado has the property id_professor of self.id
            if enunciado.id_professor == self.id:
                enunciado.delete()
                return True
            else:
                return False
            
    # Somente o professor proprietario do enunciado pode alterar o prazo de entrega
    def modificar_prazo(self, id_enunciado, data_entrega):
        enunciado = EnunciadoModel.find(id_enunciado)
        if enunciado:
            if enunciado.id_professor == self.id:
                return enunciado.modificar_prazo(data_entrega)
        else:
            return False

    def modificar_enunciado(self, id_enunciado, titulo, descricao, data_entrega):
        enunciado = EnunciadoModel.find(id_enunciado)
        if enunciado:
            if enunciado.id_professor == self.id:
                return enunciado.modificar_enunciado(titulo, descricao, data_entrega)
        else:
            return False
    



    @classmethod
    def find(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod   
    def findAll(cls):
        return cls.query.all()

    def update(self, nome):
        self.nome = nome
        self.save()


class AlunoModel(db.Model):
    __tablename__ = "tbl_aluno"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))

    def __init__(self, nome, **kwargs):
        self.nome = nome
        super(AlunoModel, self).__init__(**kwargs)

    def toDict(self):
        return {'id': self.id, 'nome':self.nome}

    def __repr__(self):
        return f"Aluno(id={self.id}, nome={self.nome})"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # verificar se o aluno já criou uma tarefa para o enunciado
    def criar_tarefa(self, id_enunciado, resposta):
        enunciado = EnunciadoModel.find(id_enunciado)
        if enunciado:
            # verificar se o aluno já criou uma tarefa para o enunciado
            tarefa = TarefaModel.findFromIdAlunoAndIdEnunciado(self.id, id_enunciado)
            if tarefa:  # se já existe uma tarefa para o enunciado
                return False
            else:
                # verifica se esta dentro do prazo de entrega
                data_entrega = enunciado.data_entrega# datetime.strptime(enunciado.data_entrega, "%Y-%m-%d")
                if data_entrega > datetime.now().date():
                    tarefa = TarefaModel(id_aluno=self.id, id_enunciado=id_enunciado, resposta=resposta)
                    tarefa.save()
                    return tarefa
                else:
                    return False


    def deletar_tarefa(self, id_tarefa):
        tarefa = TarefaModel.find(id_tarefa)
        if tarefa:
            if tarefa.id_aluno == self.id:
                return tarefa.delete()
            else:
                return False


 

    def update(self, nome):
        self.nome = nome
        self.save()

    @classmethod
    def find(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod   
    def findAll(cls):
        return cls.query.all()



class EnunciadoModel(db.Model):
    __tablename__ = "tbl_enunciado"

    id = db.Column(db.Integer, primary_key=True)
    id_professor = db.Column(db.Integer, db.ForeignKey('tbl_professor.id'))
    titulo = db.Column(db.String(120))
    descricao = db.Column(db.String(1000))
    data_entrega = db.Column(db.Date)


    def __init__(self, id_professor, titulo, descricao, data_entrega, **kwargs):
        self.id_professor = id_professor
        self.titulo = titulo
        self.descricao = descricao
        self.data_entrega = datetime.strptime(data_entrega, "%Y-%m-%d")
        super(EnunciadoModel, self).__init__(**kwargs)

    def toDict(self):
        return {'id': self.id, 'id_professor':self.id_professor, 'titulo':self.titulo, 'descricao':self.descricao, 'data_entrega':self.data_entrega.strftime("%Y-%m-%d")}

    def __repr__(self):
        return f"Enunciado(id={self.id}, id_professor={self.id_professor}, titulo={self.titulo}, descricao={self.descricao}, data_entrega={self.data_entrega.strftime('%Y-%m-%d')})"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def modificar_enunciado(self, titulo, descricao, data_entrega):
        self.titulo = titulo
        self.descricao = descricao
        self.data_entrega = datetime.strptime(data_entrega, "%Y-%m-%d")
        try:
            self.save()
            return self
        except:
            return False


    def modificar_prazo(self, data_entrega):
        self.data_entrega = datetime.strptime(data_entrega, "%Y-%m-%d")
        self.save()
        try:
            self.save()
            return self
        except:
            return False
    

    @classmethod
    def find(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def findOneFromProfessor(cls, id_professor, id_enunciado):
        return cls.query.filter_by(id_professor=id_professor, id=id_enunciado).first()

    @classmethod   
    def findAll(cls):
        return cls.query.all()

    @classmethod
    def findAllFromProfessor(cls, id_professor):
        return cls.query.filter_by(id_professor=id_professor).all()









