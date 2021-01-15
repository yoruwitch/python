# Faça um programa que leia um número inteiro e mostre na tela seu antecessor e sucessor.

n1 = int(input("Digite um número: "))
ant = int(n1 - 1)
suc = int(n1 + 1)

print("O número {} tem como antecessor {} e sucessor {}.".format(n1, ant, suc))
