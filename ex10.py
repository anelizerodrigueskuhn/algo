valor_compra = float(input("insira o valor da compra"))

if valor_compra >= 100:
    desconto = 0.10 #desconto de 10%
    valor_com_desconto = valor_compra * (1 - desconto)
    print(f"desconto apliacado: 10%")
    print(f"valor final da compra: {valor_com_desconto}")
else:
    print("sem desconto")
    print(f"valor final da compra: {valor_compra}")
