"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
separadamente. """

nome = str(input("Digite seu nome completo: ")).strip()
nome2 = nome.split(" ")
print("Seu nome completo é: {}. ".format(nome))
print("Seu primeiro nome é: {}.".format(nome2[0]))
print("Seu último sobrenome é: {}.".format(nome2[-1]))
