import math 
cateto_oposto = float(input('digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('digite o comprimento do cateto adjacente: '))
hipotenuza = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)
print(f'o comprimento da {hipotenuza:.2f}')