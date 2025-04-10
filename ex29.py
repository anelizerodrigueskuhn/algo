#Multiplicação de Elementos da Lista
# Crie uma lista chamada valores com 4 números inteiros fornecidos pelo usuário.
# Peça ao usuário um número adicional e multiplique cada elemento da lista pelo número fornecido, usando um laço for.
# Exiba os novos valores da lista.

valores = []
for i in range(4):
    valor = int(input("Digite um número: "))
    valores.append(valor)

numero = int(input("Digite um número adicional: "))

for i in range(len(valores)):
    valores[i] *= numero

print("Novos valores da lista:", valores)
