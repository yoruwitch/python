#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input("Digite um numero: "))
par = numero % 2
if numero == par:
    print("Esse número é PAR.")
else:
    print("Esse número é IMPAR.")