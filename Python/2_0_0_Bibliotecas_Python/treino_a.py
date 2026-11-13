import math

def recebe_raio():
    while True:
        try:
            numero = float(input("digite o raio da mesa em metros: ").replace(",", "."))
            break
        except:
            print("Número inválido, por favor, digite apenas números!")
    return numero

def calcula_area(raio):
    area = math.pi * math.pow(raio, 2)
    return area

raio = recebe_raio()
area = round(calcula_area(raio), 2)
print("a area da mesa é: ", area, "Mt2")
