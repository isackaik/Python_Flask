import sqlalchemy.exc
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from models import Usuarios
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS, cross_origin

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)
CORS(app)
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Documentação da API"
    },
    # oauth_config={  # OAuth config. See https://github.com/isackaik/Python_Flask.git .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)

Roles = {
    'professor': 'professor'
}

@auth.verify_password
def autenticacao(login, senha):
    if not (login, senha):
        return False
    return Roles.get(login) == senha


class Usuario(Resource):
    @cross_origin()
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
                'mensagem': 'Usuario nao encontrado.'
            }

        return jsonify(response)

    @cross_origin()
    @auth.login_required
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
                'mensagem': 'Usuario nao encontrado.'
            }

        return jsonify(response)

    @cross_origin()
    @auth.login_required
    def delete(self, cpf):
        user = Usuarios.query.filter_by(cpf=cpf).first()
        try:
            mensagem = 'Usuario {} excluido com sucesso'.format(user.cpf)
            user.delete()
            response = {
                'status': 'Sucesso',
                'mensagem': mensagem
            }

        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Usuario nao encontrado.'
            }

        return response

class CreateUser(Resource):

    @cross_origin()
    @auth.login_required
    def post(self):
        dados = request.json
        try:
            user = Usuarios(cpf=dados['cpf'], nome=dados['nome'], data_nascimento=dados['data_nascimento'])
            user.save()
            response = {
                'cpf': user.cpf,
                'nome': user.nome,
                'data de nascimento': user.data_nascimento
            }
        except sqlalchemy.exc.IntegrityError:
            response = {
                'status': 'error',
                'mensagem': 'CPF já cadastrado.'
            }
        except KeyError:
            response = {
                'status': 'error',
                'mensagem': 'Corpo da requisição inválida.'
            }

        return jsonify(response)


api.add_resource(Usuario, '/usuario/<string:cpf>/')
api.add_resource(CreateUser, '/usuario/')


if __name__ == '__main__':
    app.run(debug=True)