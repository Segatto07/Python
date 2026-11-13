try:
    saldo = 1000 

    print("1 - Consultar saldo ")
    print("2 - Depositar ")
    print("3 - Sacar ")
    print("4 - Sair ") 

    menu = int(input("Digite uma das opções acima! : "))

    match menu:
        case 1:
            print("Seu saldo é", saldo)
        case 2: 
            vdeposito = float(input("Digite a valor a ser depositado: ").replace(",","."))
            resultado = saldo + vdeposito
            print("Você depositou", vdeposito, "e seu saldo é = ", resultado)
except:
    print("Numero inválido. Por favor, informe somente números inteiros")
