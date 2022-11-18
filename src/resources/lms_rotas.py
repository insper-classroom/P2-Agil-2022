from flask_restful import Resource
from flask import request
from model.lms_models import ProfessorModel, AlunoModel, TarefaModel, EnunciadoModel


class ListaProfessores(Resource):
    # return all professors from ProfessorModel

    def get(self):
        return {'professores': [professor.toDict() for professor in ProfessorModel.findAll()]}


class Professor(Resource):

    def get(self, id):
        prof = ProfessorModel.find(id)
        if prof:
            return prof.toDict()
        return {'mensagem': 'Professor nao encontrado'}, 404
    
    def post(self):
        data = request.get_json()
        prof = ProfessorModel(**data)
        try:
            prof.save()
        except:
            return {'mensagem': 'Ocorreu um erro ao tentar inserir um professor'}, 500
        return prof.toDict(), 201

    def put(self, id):
        data = request.get_json()
        prof = ProfessorModel.find(id)
        if prof:
            prof.update(**data)
            return prof.toDict(), 200
        return {'mensagem': 'Professor nao encontrado'}, 404

    def delete(self, id):
        prof = ProfessorModel.find(id)
        if prof:
            prof.delete()
            return {'mensagem': 'Professor deletado'}
        return {'mensagem': 'Professor nao encontrado'}, 404

class ListaAlunos(Resource):

    def get(self):
        return {'alunos': [aluno.toDict() for aluno in AlunoModel.findAll()]}

class Aluno(Resource):
    
    def get(self, id):
        aluno = AlunoModel.find(id)
        if aluno:
            return aluno.toDict()
        return {'mensagem': 'Aluno nao encontrado'}, 404
    
    def post(self):
        data = request.get_json()
        aluno = AlunoModel(**data)
        try:
            aluno.save()
        except:
            return {'mensagem': 'Ocorreu um erro ao tentar inserir aluno'}, 500
        return aluno.toDict(), 201

    def put(self, id):
        data = request.get_json()
        aluno = AlunoModel.find(id)
        if aluno:
            aluno.update(**data)
            return aluno.toDict(), 200
        return {'mensagem': 'Aluno nao encontrado'}, 404

    def delete(self, id):
        aluno = AlunoModel.find(id)
        if aluno:
            aluno.delete()
            return {'mensagem': 'Aluno deletado'}
        return {'mensagem': 'Aluno nao encontrado'}, 404





class ListaEnunciados(Resource):

    def get(self):
        return {'enunciados': [enunciado.toDict() for enunciado in EnunciadoModel.findAll()]} 


class Enunciado(Resource):
            

    def get(self, id_professor):
        # get all statements from a professor
        return {'enunciados': [enunciado.toDict() for enunciado in EnunciadoModel.findAllFromProfessor(id_professor)]}

    def post(self, id_professor):
        data = request.get_json()
        professor = ProfessorModel.find(id_professor)
        if professor:
            try:
                enunciado = professor.criar_enunciado(**data)
            except:
                return {'mensagem': 'Ocorreu um erro ao tentar inserir um enunciado'}, 500

        return enunciado.toDict(), 201
    
    def put(self, id_professor, id_enunciado):
        data = request.get_json()
        # check if the key "data_entrega" is the only key inside data
        if len(data) == 1 and 'data_entrega' in data:
            professor = ProfessorModel.find(id_professor)
            if professor:
                try:
                    enunciado = professor.modificar_prazo(id_enunciado, data['data_entrega'])
                except:
                    return {'mensagem': 'Ocorreu um erro ao tentar atualizar a data de entrega'}, 500
                return enunciado.toDict(), 200
        else:
            professor = ProfessorModel.find(id_professor)
            if professor:
                try:
                    enunciado = professor.modificar_enunciado(id_enunciado, **data)
                except:
                    return {'mensagem': 'Ocorreu um erro ao tentar atualizar o enunciado'}, 500

                #check if enunciado is bool or EnunciadoModel
                if isinstance(enunciado, bool):
                    return {'mensagem': 'Ocorreu um erro ao tentar atualizar o enunciado'}, 404
                else:
                    return enunciado.toDict(), 200
        return {'mensagem': 'Ocorreu um erro ao tentar atualizar o enunciado'}, 500          



    def delete(self, id_professor, id_enunciado):
        enunciado = EnunciadoModel.findOneFromProfessor(id_professor, id_enunciado)
        if enunciado:
            try:
                enunciado.delete()
                return {'mensagem': 'Enunciado deletado'}
            except:
                return {'mensagem': 'Ocorreu um erro ao tentar deletar um enunciado'}, 500
            
        return {'mensagem': 'Enunciado nao encontrado'}, 404

