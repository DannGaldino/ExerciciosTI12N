def exer6():
    print("Informe o seu salário mensal atual: ")
    salario = float(input())
    print("Informe o percentual de reajuste do seu  salário: ")
    reajuste = float(input())
    novoSalario = salario + (salario * (reajuste / 100))
    print("Seu novo salário será: " + str(novoSalario))
