def exer5():
    print("Informe o número de votos brancos: ")
    brancos = int(input())
    print("Informe o número de votos núlos: ")
    nulos = int(input())
    print("Informe o número de votos válidos: ")
    validos = int(input())
    total = (brancos + nulos + validos)
    percBrancos = brancos / total
    percNulos = nulos / total
    percValidos = validos / total
    print("Total de eleitores : " + str(total) + "\nPercentual de votos brancos: " + str(percBrancos * 100) + "%\nPercentual de votos núlos: " + str(percNulos * 100) + "%\nPercentual de votos válidos: " + str(percValidos * 100) + "%")
