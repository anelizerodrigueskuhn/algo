#Lista de Nomes
# Crie uma lista chamada nomes e insira os nomes de 5 amigos.
# Use um laço for para exibir os nomes em ordem alfabética.

nomes = []

for i in range(5):
    nome = input("Digite o nome de um amigo: ")
    nomes.append(nome)

nomes.sort()

for nome in nomes:
    print(nome)


