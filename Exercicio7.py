def exer7():
    print("Informe o custo de fabrica do automóvel: ")
    fabrica = float(input())
    print("Informe a porcentagem do distribuidor: ")
    distribuidor  = float(input())
    print("Informe a porcentagem dos impostos: ")
    impostos = float(input())
    valorFinal = (fabrica + (fabrica * (distribuidor / 100)) + (fabrica * (impostos / 100)))
    print("O valor final do veiculo é: R$" + str(valorFinal))
