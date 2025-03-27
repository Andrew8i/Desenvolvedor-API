from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades,habilidades,Habilidades_id


#Lista de desenvolvedores
desenvolvedores =[{'id':0,'nome':'Andre','Habilidades': ['Python', 'Flask']},{'id':1,
'nome':'João','Habilidades': ['Python', 'Django']}]

#Inclui em variáveis as instâncias do Flask e APi
app = Flask (__name__)
api = Api(app)

#Classe Desenvolvedor que tem os métodos get,put e delete recebendo id como parametro para respectivamente obter informações do desenvolvedor correspondente ao id, modificar o desenvolvedor correspondente ao id, deletar o desenvolvedor que corresponde ao id
class Desenvolvedor(Resource):
    def get(self,id):
        try:
            response = desenvolvedores[id]

        except IndexError:
            mensagem = 'Desenvolvedor não existe'
            response = {'status': 'erro', 'mensagem': mensagem}

        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status': 'erro', 'mensagem': mensagem}

        return (response)
    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return (dados)
    def delete(self,id):
        desenvolvedores.pop(id)
        return {'status':'sucesso','mensagem': 'registro excluído'}

#Classe Desenvolvedor_Post que tem os métodos post e get, que respectivamente posta um novo desenvolvedor se a habilidade constar na lista de habilidades, e mostrar todos os desenvolvedores
class Desenvolvedor_Post(Resource):
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        for i in habilidades:
            if dados['Habilidades'] in habilidades:
                desenvolvedores.append(dados)
                return 'Habilidades constam na listam, Usuario adicionado com sucesso'
                break
            else:
                return "Essas Habilidades não constam na lista de habilidades, adicione novas habilidades ou escolha outras"
    def get(self):
        return (desenvolvedores)

#Rotas da Api
api.add_resource(Desenvolvedor, '/<int:id>/')
api.add_resource(Desenvolvedor_Post, '/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(Habilidades_id, '/habilidades/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)