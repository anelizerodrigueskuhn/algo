email_certo = input("crie um email:")
email_certto = str.lower(email_certo)

senha=input("crie uma senha")
if len(senha) < 8:
    print("senha muito pequena")
else:
    senha_certa = senha
    email=input("insira o email")
    senha=input("insira a senha")
    if email == senha_certa:
        print("bem vindo")
    else:
        print("email ou senha incorretos")


