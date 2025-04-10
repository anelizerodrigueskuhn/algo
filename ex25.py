#Jogo de Adivinhação com Vetores
# Crie um programa onde o computador sorteia um número entre 1 e 20.
# Armazene os palpites do usuário em uma lista chamada palpites.
# Use um laço while para permitir que o usuário continue tentando até acertar.
# Ao final, exiba todos os palpites que o usuário forneceu.

import random

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
palpites = []

while True:
    palpite = random.choice(numeros)
    palpites.append(palpite)
    print(f"Palpite: {palpite}")
    if palpite == 10:
        break