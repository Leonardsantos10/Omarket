import modulo2
import json

pessoa = dict()


def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, "w")
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo!")
    else:
        print("Arquivo", nome,"criado com sucesso!")

def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler o arquivo!")
    else:
        modulo1.cabeçalho("CADASTRO DE INFORMAÇÕES")
        print(a.read())
    finally:
        a.close()



def carregar_json(arq):
    with open(arq, 'r+') as f:
        return json.load(f)



def cadastrar(arq, nome, cpf, endereco, moeda):

    with open(arq) as json_file:
            data = json.load(json_file)
            dados = {"Nome":nome,"CPF":cpf,"Endereco":endereco, "Moeda":moeda}
            data.append(dados)
            write_json(data)
            print("Novo registro de", nome," adicionado")
                

def write_json(data, filename="meu_cadastro.json"):
    with open (filename,"w") as f:
        json.dump(data,f,indent=4)
        f.close()
    
            
