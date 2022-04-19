import this
import Exercicio1
import Exercicio2
import Exercicio3
import Exercicio4
import Exercicio5
import Exercicio6
import Exercicio7
import Exercicio8
import Exercicio9

this.opcao = 0
this.num1 = 0
this.num2 = 0

def mostrarMenu():
    print("-----Menu-----\n1.Exercício 1\n2.Exercício 2\n3.Exercício 3\n4.Exercício 4\n5.Exercício 5\n6.Exercício 6\n7.Exercício 7\n8.Exercício 8\n9.Exercício 9\n10.Exercício 10\n11.Exercício 11\n12.Exercício 12\n13.Exercício 13\n14.Exercício 14\n15.Exercício 15\n16.Exercício 16\n17.Exercício 17\n18.Exercício 18\n19.Exercício 19\n20.Exercício 20\n21.Sair\n\nEscolha uma das opções acima:")
    this.opcao = int(input())

def operacao():
    while this.opcao != 21:
        mostrarMenu()
        if this.opcao == 1:
            Exercicio1.exer1()
        elif this.opcao == 2:
            Exercicio2.exer2()
        elif this.opcao == 3:
            Exercicio3.exer3()
        elif this.opcao == 4:
            Exercicio4.exer4()
        elif this.opcao == 5:
            Exercicio5.exer5()
        elif this.opcao == 6:
            Exercicio6.exer6()
        elif this.opcao == 7:
            Exercicio7.exer7()
        elif this.opcao == 8:
            Exercicio8.exer8()
        elif this.opcao == 9:
            Exercicio9.exer9()
        else: print("Opção Escolhida Inválida, tente outro número!")
