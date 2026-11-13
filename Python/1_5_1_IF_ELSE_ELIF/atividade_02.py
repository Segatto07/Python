try:
    nota = int(input("Digite sua nota: "))
    if nota >=7 and nota <=10:
        print("Parabéns você foi aprovado!")
    elif nota >=5 and nota <=6.9:
        print("Ah infelizmente você está de recuperção, foco você consegue!")  
    elif nota >0 and nota <=4.9:
        print("Você reprovou, estude mais! Confio no seu potencial!")      
    else:
        print("Nota inválida.")

except:
    print("Digite apenas números!")