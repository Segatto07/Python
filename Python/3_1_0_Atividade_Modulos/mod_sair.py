from mod_inputs import inp_str

def finalizar():
    start = True
    while start:
        try: 
            opcao = inp_str("\n Deseja finalizar o programa? S/N: ")
            if opcao in("s", "S") or opcao in ("n", "N"):
                break
            else:
                print("Opção invlida! \n")

        except:
            print("Valor inválido.", "\n")

    if opcao in("s", "S"):
        print("\n Programa encerrado!")

        return False
    else:
        return True



