import pymongo
import json
import arquivosprod
arq2 = "meu_cadastro2.json"
c = 0

def bancoprodutor():
    cluster = pymongo.MongoClient("mongodb+srv://db_user:DGZFdRXUsvFe5NRB@cluster0.3cfxm.mongodb.net/clientes?retryWrites=true&w=majority")

    db = cluster.get_database('python')

    collection = db.get_collection('produtores')

    retorno1 = arquivosprod.carregar_json(arq2)
    print(retorno1)

    dados = retorno1


    for dado in dados:
        print(dado)
        collection.insert_many([dado])
