'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos
e escrevendo na tela o nome do escolhido.'''
import random

aluna = input("Digite o nome do aluno: ")
alunb = input("Digite o nome do aluno: ")
alunc = input("Digite o nome do aluno: ")
alund = input("Digite o nome do aluno: ")
lista = [aluna, alunb, alunc, alund]
print("Parabéns, {}! Você vai apagar o quadro pro professor.". format(random.choice(lista)))
