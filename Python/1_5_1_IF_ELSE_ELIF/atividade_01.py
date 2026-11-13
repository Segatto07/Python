try:
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print("você já é adulto!")
    elif idade >=13 and idade <=17:
        print("Você é adolescente!")  
    elif idade >0 and idade <=12:
        print("Você é uma criança!")     
    else:
        print("Idade inválida") 

except:
    print("Digite apenas números!")