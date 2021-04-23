from flask_restful import Resource
from flask import request
import json

lista_habilidades = ['Python', 'Java', 'PhP', 'Flask', 'Ruby']
class Habilidades(Resource):
    def get(self):
        return lista_habilidades
    def post(self):
        hab = json.loads(request.data)
        lista_habilidades.append(hab)
        return(lista_habilidades)

class Habilidade(Resource):
    def get(self, id):
        try:
            response = lista_habilidades[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} nao existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o adm da API'
            response = {'status': 'Erro', 'mensagem': mensagem}
        return response
    def put(self, id):
        hab = json.loads(request.data)
        lista_habilidades[id] = hab
        return lista_habilidades
    def delete(self, id):
        lista_habilidades.pop(id)
        return lista_habilidades
