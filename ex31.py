numero = int(input("digite um numero"))
# codico em python para exibir as tabuads de 7,8 e 9
def tabuada(numero):
    print(f"tabuada do{numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# exibindo as tabelas
tabuada(numero)