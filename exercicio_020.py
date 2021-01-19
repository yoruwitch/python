'''O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

import random

aluna = str(input("Digite o nome do aluno: "))
alunb = str(input("Digite o nome do aluno: "))
alunc = str(input("Digite o nome do aluno: "))
alund = str(input("Digite o nome do aluno: "))
lista = [aluna, alunb, alunc, alund]
random.shuffle(lista)
print("A ordem de apresentação dos trabalhos é: ")
print(lista)

