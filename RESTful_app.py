from flask import Flask, request
from flask_restful import Resource, Api
from Habilidades import Habilidades, Habilidade, lista_habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
     'id': 0,
     'nome': 'Cleber',
     'habilidades': ['Python', 'Flask']
    },
    {'id': 1,
     'nome':'Luan',
     'habilidades': ['Python', 'Django']
    }
]

#list_hab = lista_habilidades

#Devolve um desenvolvedor pelo ID, tambem altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} nao existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o adm da API'
            response = {'status': 'Erro', 'mensagem': mensagem}
        return response
    def put(self, id):
        dados = json.loads(request.data)
        if dados['habilidades'] in lista_habilidades:
            desenvolvedores[id] = dados
            return dados
        else:
            return {'{} não é uma habilidade existente'.format(dados['habilidades'])}
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}

#Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        sum = 0
        for x in dados['habilidades']:
            if x in lista_habilidades:
                sum = sum + 1
            else:
                return '{} não é uma habilidade existente'.format(x)
        if sum == len(dados['habilidades']):
            desenvolvedores.append(dados)
            return desenvolvedores

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(Habilidade, '/habilidades/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)
