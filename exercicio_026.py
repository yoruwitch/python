"""Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez."""

frase = str(input("Diga alguma coisa: ")).upper().strip()
frase2 = frase.replace('Á', 'A').replace('Â', 'A')
print("A letra {} aparece vez(es) na frase.".format(frase.count("A")))
print("A letra A aparece pela primeira vez na posição {}.".format(frase.find("A")+1))
print("A letra A aparece pela última vez na posição {}.".format(frase.rfind("A")+1))
