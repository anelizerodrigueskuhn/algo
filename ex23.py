#Tabuada com Vetores
# Peça ao usuário para digitar um número inteiro.
# Crie uma lista chamada tabuada que contenha os resultados da tabuada desse número (1 a 10).
# Use o laço for para preencher a lista com os resultados e depois exiba os valores armazenados.

numero = int(input("Digite um número inteiro: "))
tabuada = []

for i in range(1, 11):
    resultado = numero * i
    tabuada.append(resultado)

print("Tabuada de", numero)
for i in range(1, 11):
    print(f"{numero} x {i} = {tabuada[i-1]}")