# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
# perdeu.
"""import random
print("Bem vindo ao jogo da adivinhação!")
n = int(input("Digite um número: "))
pc = [0, 1, 2, 3, 4, 5]
if n == random.choice(pc):
    print("Uau, você acertou! Parabéns!!")
else:
    print("Poxa, você errou, tente de novo!")"""

from random import randint
from time import  sleep
print("-=-"*13)
print("Bem vindo ao jogo de adivinhação!")
print("-=-"*13)
print("Tente adivinhar um número que eu pensei.")
jogador = int(input("Escolha um número: "))
comp = randint(0, 5)
print("PROCESSANDO...")
sleep(3)
if jogador == comp:
    print("Uau você adivinhou, seu danado!")
else:
    print("Ah não! Eu pensei no número {} e você no número {}. Eu ganhei HAH!".format(comp, jogador))
print("----FIM DO JOGO ----")
