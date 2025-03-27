status_conta = True

valor_saldo= int(input("digite seu saldo no banco"))
if valor_saldo >=0.01:
    print("sua conta ainda esta ativa:")
elif valor_saldo <0:
    print ("renegociar a divida")
else:
    status_conta = False
    print("conta inativa")