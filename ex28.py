#Filtrando Números Pares e Ímpares
# Crie uma lista chamada numeros com 8 números inteiros escolhidos pelo usuário.
# Use um laço for para dividir os números em duas listas: pares e impares.

numeros = []
for i in range(8):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números pares:", pares)
print("Números impares:", impares)
