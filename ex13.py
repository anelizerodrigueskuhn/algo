#cadastro de um aluno em uma escola
nome = input("insira seu nome:")
idade = int(input("insira sua idade:"))
turma = input("insira sua turma:")

if idade>=6:
    print(f"aluno cadastrado com sucesso: {nome}, {idade} anos, {turma}")
else:
    print("aluno não tem idade sulficiente  para entrar na escola")