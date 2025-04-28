base, inicio, fim = int(input("digite um numero:")), int(input("digite o intervalo da tabuada (ex: 1-10:)"))
int(input("digite o final (ex: 1-10)"))
def tabuada_personalizada(base, inicio, fim):
    print(f"tabuada do {base} de {inicio} a {fim}")
    for j in range(inicio, fim + 1):
        print(f"{base} x {j} = {base * j}")

# uso
tabuada_personalizada(base, inicio, fim)