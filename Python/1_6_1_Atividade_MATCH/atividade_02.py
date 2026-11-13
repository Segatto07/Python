try:
    semana = int(input("Informe um dia da semana em numeros de 1 a 7: "))

    match semana:
        case 1:
            print("Segunda - feira")
        case 1:
                print("Segunda - Feira")
        case 2:
                print("Terça - Feira")
        case 3:
                print("Quarta - Feira")
        case 4:
                print("Quinta - Feira")
        case 5:
                print("Sexta - Feira")
        case 6:
                print("Sabado")
        case 7:
                print("Domingo")
        case _:
            print("Dia da semana inválido!")
            
except:
       print("Valor informado inválido, por favor, digite apenas números inteiros! ")     
             