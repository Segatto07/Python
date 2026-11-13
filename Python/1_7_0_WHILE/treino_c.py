nomes = []

while True: 
    print("1 -cadastro")
    print("2 - Consulta")
    print("3 - Relatótio")
    print('4 - Sair')

    try:
        menu = int(input("Digite alguma das opções acima! :"))
    except:
        print("Opção inválida. Digite apenas as opções acima (1 a 4)!")
    if menu == 1:
        nome = input("Seu nome:")
        nomes.append(nome)
        print("Cadastrado!")
    elif menu == 2:
        nome = input(" Digite o nome para a consulta: ")
        if nome in nomes:
            print("achei!")
        else: 
            print("não está cadastrado")
    elif menu == 3:
        print("pessoas cadastradas: ")
        for nome in nomes:
            print("total", len(nomes))
    elif menu == 4:
        print("Bye, bye")
        break
    else:
        print("escolha uma das opções de 1 a 4")


