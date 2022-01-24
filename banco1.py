import pymongo
import json
import arquivos2
arq = "meu_cadastro.json"
c = 0

def banco_de_dados():
    cluster = pymongo.MongoClient("mongodb+srv://db_user:DGZFdRXUsvFe5NRB@cluster0.3cfxm.mongodb.net/clientes?retryWrites=true&w=majority")

    db = cluster.get_database('python')

    collection = db.get_collection('clientes')

    retorno = arquivos2.carregar_json(arq)

    dados = retorno


    for dado in dados:
        print(dado)
        collection.insert_many([dado])

