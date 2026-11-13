from datetime import datetime, timedelta

def recebe_data():
    start = True
    while start:
        try:
            data = input("Infome sua data da compra em (DD/MM/AAAA): ")
            data_compra = datetime.strptime(data, "%d/%m/%Y")
            if data_compra.date() > datetime.now().date():
                print("A data de compra não pode ser futura! ")
            else:
                return data_compra
        except ValueError:
            print("Data incorreta. Por favor, infome a da em DD/MM/AAAA)")
            
def concular_prazo(data_compra, dias=7):
    entrega = data_compra + timedelta(days=dias)
    restantes = (entrega.date() - datetime.now().date()).days
    return entrega, restantes

data_compra = recebe_data()
entrega, restantes = concular_prazo(data_compra, dias=7)

print("Data do pedido", data_compra.strftime("%d/%m/%Y"))
print("Data de hoje", datetime.now().strftime("%d/%m/%Y"))
print("Previsão de entrega ", entrega.strftime("%d/%m/%Y"))

if restantes > 0:
    print("Faltam", restantes, "dias")
elif restantes == 0:
    print("A entrega é hoje!")
else:
    print("O seu prazo já passou há", abs(restantes), "dias")

