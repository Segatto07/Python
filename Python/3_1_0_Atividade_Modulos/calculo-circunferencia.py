import math
import mod_inputs

def recebe_raio():
    while True:
        try:
            numero = float(input("digite o raio da mesa em metros: ").replace(",", "."))
            break
        except:
            print("Número inválido, por favor, digite apenas números!")
    return numero

def calcula_area(raio):
    area = 2 * math.pi * math.pow(raio)
    return area

raio = recebe_raio()
area = round(calcula_area(raio))
print("a area da mesa é: ", area, "Mt2")