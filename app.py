from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from models import Usuarios

app = Flask(__name__)
api = Api(app)

class Usuario(Resource):
    def get(self, cpf):
        user = Usuarios.query.filter_by(cpf=cpf).first()
        try:
            response = {
                'cpf': user.cpf,
                'nome': user.nome,
                'data de nascimento': user.data_nascimento
            }
        except AttributeError:
            response = {
                'status': 'error',
                'message': 'Usuario nao encontrado '
            }

        return jsonify(response)

    def put(self, cpf):
        user = Usuarios.query.filter_by(cpf=cpf).first()
        try:
            dados = request.json
            if 'nome' in dados:
                user.nome = dados['nome']
            if 'data_nascimento' in dados:
                user.data_nascimento = dados['dados_nascimento']
            user.save()
            response = {
                'cpf': user.cpf,
                'nome': user.nome,
                'data de nascimento': user.data_nascimento
            }

        except AttributeError:
            response = {
                'status': 'error',
                'message': 'Usuario nao encontrado '
            }

        return jsonify(response)

    def delete(self, cpf):
        user = Usuarios.query.filter_by(cpf=cpf).first()
        try:
            mensagem = 'Usuario {} excluido com sucesso'.format(self, user.cpf)
            user.delete()
            response = {
                'status': 'Sucesso',
                'message': mensagem
            }

        except AttributeError:
            response = {
                'status': 'error',
                'message': 'Usuario nao encontrado '
            }

        return response

class CreateUser(Resource):
    def post(self):
        dados = request.json
        user = Usuarios(cpf=dados['cpf'], nome=dados['nome'], data_nascimento=dados['data_nascimento'])
        user.save()
        response = {
            'cpf': user.cpf,
            'nome': user.nome,
            'data de nasccimento': user.data_nascimento
        }

        return jsonify(response)


api.add_resource(Usuario, '/usuario/<string:cpf>/')
api.add_resource(CreateUser, '/usuario/')


if __name__ == '__main__':
    app.run(debug=True)