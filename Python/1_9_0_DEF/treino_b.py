def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3  
    return media

def receber_nota(mensagem):
    start = True
    while start:
        try:
            nota1 = float(input(mensagem).replace(".","."))
            start = False
          
        except:
            print("Nota incorreta. Por favor insira apenas números.")
    return nota1

def situacao(media):
    try:
   
        if media >=7:
            mensagem = "Aprovado"
        else:
            mensagem = "reprovado"
        return mensagem
    
    except:
        print("informe apenas numeros")

    
nota1 = receber_nota("Digite a primeira nota: ") 
nota2 = receber_nota("Digite a segunda nota: ") 
nota3 = receber_nota("Digite a terceira nota: ") 

media = calcular_media(nota1, nota2, nota3)
situacao1 = situacao(media)
print("sua média é = ", media)
print("você foi", situacao1)
