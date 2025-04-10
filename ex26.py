#Cálculo de Média
# Crie uma lista chamada notas com as notas de 5 alunos fornecidas pelo usuário.
# Use um laço for para calcular a média das notas.
# Exiba a média no final.

notas = []
for i in range(5):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Média das notas:", media)
