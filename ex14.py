#login bancário. crie um sistema de login simples
usuario = input("insira o nome do usuario:")
senha = input("insira a senha:")

if usuario == "admin" and senha == "1234":
    print("login efetuado com sucesso")
else:
    print("login ou senha incorretos")