'''Faça um programa que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

from math import radians, sin, cos, tan
ang = float((input(("Digite o ângulo: "))))
sen = sin(radians(ang))
print("O SENO de {} é {:.2f}.".format(ang, sen))
cos = cos(radians(ang))
print("O COSSENO de {} é {:.2f}.".format(ang, cos))
tan = tan(radians(ang))
print("A TANGENTE de {} é {:.2f}".format(ang, tan))
