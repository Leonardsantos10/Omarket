def leiaInt(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print("ERRO: Por favor, digite um número inteiro válido.")
            continue
        except (KeyboardInterrupt):
            print("\nUsuário não digitou nenhum número.")
            return 0
        else:
            return n

def linha(tam=42):
    return "-" * tam

def cabeçalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())

def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(c, "-", item)
        c += 1
    print(linha())
    opção = leiaInt("Escolha uma opção: ")
    return opção


nome1 = "Alface"
nome2 = "Tomate"
nome3 = "Cebola"
nome4 = "Banana"
nome5 = "Mamão"
nome6 = "Maçã"
nome7 = "Couve"
nome8 = "Arroz"
nome9 = "feijão"
nome10 = "Batata"

def criarTabela():

    print("Produto\t\tValor em Seeds")
    print(linha())
    print("%s:\t\t%d"%(nome1, 10),"Seeds")
    print("%s:\t\t%d"%(nome2, 20),"Seeds")
    print("%s:\t\t%d"%(nome3, 30),"Seeds")
    print("%s:\t\t%d"%(nome4, 40),"Seeds")
    print("%s:\t\t%d"%(nome5, 30),"Seeds")
    print("%s:\t\t%d"%(nome6, 10),"Seeds")
    print("%s:\t\t%d"%(nome7, 20),"Seeds")
    print("%s:\t\t%d"%(nome8, 50),"Seeds")
    print("%s:\t\t%d"%(nome9, 50),"Seeds")
    print("%s:\t\t%d"%(nome10, 20),"Seeds")
    print(linha())
    print("A cada 1 kg de lixo orgânico, são ganhos 10 seeds!")
    print(linha())
