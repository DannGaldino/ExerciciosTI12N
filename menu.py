import this

this.opcao = 0
this.num1 = 0
this.num2 = 0

def coletarNum1():
    print("Informe o 1° número: ")
    this.num1 = float(input())

def coletarNum2():
    print("Informe o 2° número: ")
    this.num2 = float(input())

def mostrarMenu():
    print("-----Menu-----\n1.Exercício 1\n2.Exercício 2\n3.Exercício 3\n4.Exercício 4\n5.Exercício 5\n\nEscolha uma das opções acima:")
    this.opcao = int(input())

def operacao():
    while this.opcao != 21:
        mostrarMenu()
        if this.opcao == 1:
