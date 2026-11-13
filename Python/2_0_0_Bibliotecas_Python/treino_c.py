from datetime import datetime

def recebe_data():
    start = True
    while start:
        try:
            data = str(input("Infome sua data de nascimento em (DD/MM/AAAA): "))
            data_nasc = datetime.strptime(data, "%d/%m/%Y")
            if data_nasc.date() > datetime.now().date():
                print("A data de nascimento não pode ser futura! ")
            else:
                start = False
        except ValueError: 
            print("data inválida! Por favor, infome sua data de nascimento como DD/MM/AAAA")
    return data_nasc   

def calcula_idade(data_nasc):
    hoje = datetime.now()
    idade = hoje.year - data_nasc.year
    ja_fez = (hoje.month, hoje.day) >= (data_nasc.month, data_nasc.day)
    if not ja_fez: 
        idade -= 1 
    return idade, ja_fez

data_nasc = recebe_data()
idade, ja_fez = calcula_idade(data_nasc)

print("Data de nascimento", data_nasc.strftime("%d/%m/%Y"))
print("Data de hoje", datetime.now().strftime("%d/%m/%Y"))
print("Sua idade é ", idade, "anos")
if ja_fez:
    print("Você já fez aniversario esse ano")
else:
    print("Você ainda não fez aniversario esse ano")

