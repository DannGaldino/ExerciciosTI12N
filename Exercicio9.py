def exer9():
    print("Informe a quantidade de maças que você quer comprar: ")
    quant = int(input())
    if quant < 12:
        valor = 1.30
    else: valor = 1
    print("Valor final: R$" + str(valor * quant))
