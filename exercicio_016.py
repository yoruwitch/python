# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

'''import math
num = float(input("Digite um número: "))
metadinha = math.modf(num)

print("O número {} tem como partes decimal e inteira {}".format(num, metadinha))'''

num = float(input("Digite um número: "))
print("O número {} tem como parte inteira {}.".format(num, int(num)))
