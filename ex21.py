#Criando e Manipulando Listas
# Crie uma lista chamada numeros com 10 números inteiros escolhidos pelo usuário.
# Use um laço for para imprimir cada número da lista.
# Calcule e exiba a soma de todos os números usando outro laço for.

numeros = []
for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

soma = 0
for numero in numeros:
    soma += numero

print("Números:", numeros)
print("Soma:", soma)
