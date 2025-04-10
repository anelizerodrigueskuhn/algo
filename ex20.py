#verificação de acesso ao clube. crie um programa em python que determine se uma pessoa pode entrar em um clube com as seguintes condições: precisa ter mais de 18 anos. se não for membro, deve pagar um ingresso. se estiver acomnhado por um membro, paga meia entrada.

idade = int(input("insira sua idade:"))
membro = input("voce eh membro?")
acompanhado = input("voce esta acompanhado?")

if idade >= 18:
    if membro == "sim": 
        print("pode entrar")
    else:
        if acompanhado == "sim":
            print("pode pagar meia entrada")
        else:
            print("pode pagar o ingresso completo")
else:
    print("voce nao pode entrar")