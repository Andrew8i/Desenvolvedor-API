from flask_restful import Resource, Api
from flask import request
import json

#Lista com as habilidades 
habilidades = ['Python','Flask','Django','PHP']

#Classe Habilidades com o metodo get que mostra as habilidades e post que pode adicionar uma nova habilidade
class Habilidades(Resource):
    def get(self):
        return(habilidades)
    def post(self):
        dados = json.loads(request.data)
        habilidades.append(dados)
        return "Nova habilidade adicionada"
    
#Classe Habilidades_id é semelhante a primeira porém nesse caso recebe o id como parametro para por meio do put modificar uma habilidade que estará na posição correspondente ao id, e o delete apagar uma habilidade na posição do id
class Habilidades_id(Resource):
    def put(self,id):
        dados = json.loads(request.data)
        posicao = id
        habilidades[posicao] = dados
        return 'Habilidade alterada com sucesso'
    def delete(self,id):
        posicao = id
        habilidades.pop(posicao)
        return "Habilidade deletada"
