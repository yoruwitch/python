"""Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo sem considerar espaços.

– Quantas letras tem o primeiro nome."""

nome = str(input("Digite o seu nome completo: ")).strip()
print("Analisando seu nome...")
print("Seu nome em maíusculas é: {}".format(nome.upper()))
print("Seu nome em minúsculas é: {}".format(nome.lower()))
print("A quantidade de caracteres é: {}".format(len(nome) -nome.count(" ")))
print("Seu primeiro nome tem {} letras.".format(nome.find(" ")))
