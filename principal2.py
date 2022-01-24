import modulo2
import arquivos2
import arquivosprod
import banco1
import bancoprod
from time import sleep

arq = "meu_cadastro.json"
arq2 = "meu_cadastro2.json"

if not arquivos2.arquivoExiste(arq):
    arquivos2.criarArquivo(arq)

if not arquivosprod.arquivoExiste(arq2):
    arquivosprod.criarArquivo(arq2)

while True:
    resposta = modulo2.menu(["Mostrar Cadastros","Cadastro de clientes", "Cadastro de produtores", "Tabela de preços", "Sair do programa"])
    if resposta == 1:
        modulo2.cabeçalho("Lista de clientes")
        retorno = arquivos2.carregar_json(arq)
        print(retorno)
        modulo2.cabeçalho("Lista de Produtores")
        retorno1 = arquivosprod.carregar_json(arq2)
        print(retorno1)
    elif resposta == 2:
        modulo2.cabeçalho("Cadastro de clientes")
        nome = str(input("Digite seu nome: "))
        cpf = float(input("Digite seu CPF: "))
        endereco = str(input("Digite seu endereço: "))
        moeda = int(input("Digite quantas moedas essa pessoa tem: "))
        arquivos2.cadastrar(arq, nome, cpf, endereco, moeda)
        banco1.banco_de_dados()
    elif resposta == 3:
        modulo2.cabeçalho("Cadastro de Produtores")
        nomeprod = str(input("Digite seu nome: "))
        cnpj = str(input("Digite seu CPF/CNPJ: "))
        enderecoprod = str(input("Digite seu edereço: "))
        arquivosprod.cadastrar(arq2, nomeprod, cnpj, enderecoprod)
        bancoprod.bancoprodutor()
    elif resposta == 4:
        modulo2.cabeçalho("TABELA DE PREÇOS")
        modulo2.criarTabela()
    elif resposta == 5:
        modulo2.cabeçalho("Saindo do sistema.. Até logo!")
        break
    else:
        print("ERRO! Digite uma opção válida.")
    sleep(2)
