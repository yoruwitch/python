'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

import math

catop = float(input("Digite o comprimento do cateto oposto (em metros): "))
cataj = float(input("Digite o comprimento do cateto adjacente (em metros): "))
print("O comprimento da hipotenusa é {} metros".format(math.hypot(cataj, catop)))
