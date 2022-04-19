def exer4():
    print("Expresse a sua idade em anos, meses e dias")
    print("Quantos anos de vida você tem?")
    anos = int(input())
    print("Quantos meses de vida você tem?")
    meses = int(input())
    print("Quantos dias de vida você tem?")
    dias = int(input())
    print("Você tem " + str((anos * 365) + (meses * 30) + dias) + "dias de vida.")
