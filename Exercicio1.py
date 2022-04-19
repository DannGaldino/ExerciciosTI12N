def exer1():
    print("Informe o valor de A:")
    a = input()
    print("Informe o valor de B:")
    b = input()
    c = b
    b = a
    a = c
    print("Valores invertidos:\nA = " + a + "\nB = " + b)
