import modulo2
import json

pessoa = dict()


def arquivoExiste(nomeprod):
    try:
        a = open(nomeprod, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nomeprod):
    try:
        a = open(nomeprod, "w")
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo!")
    else:
        print("Arquivo", nomeprod,"criado com sucesso!")

def lerArquivo(nomeprod):
    try:
        a = open(nomeprod, "rt")
    except:
        print("Erro ao ler o arquivo!")
    else:
        modulo1.cabeçalho("CADASTRO DE INFORMAÇÕES")
        print(a.read())
    finally:
        a.close()



def carregar_json(arquivo):
    with open(arquivo, 'r+') as f:
        return json.load(f)


def cadastrar(arq2, nomeprod, cnpj, enderecoprod):

    with open(arq2) as json_file1:
            data1 = json.load(json_file1)
            dados1 = {"Nome":nomeprod,"CPF/CNPJ":cnpj,"Endereco":enderecoprod}
            data1.append(dados1)
            write_json(data1)
            print("Novo registro de", nomeprod," adicionado")
                

def write_json(data1, filename1="meu_cadastro2.json"):
    with open (filename1,"w") as f:
        json.dump(data1,f,indent=4)
        f.close()
