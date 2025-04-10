#simulação de compra no mercado. desenvolva um programa que: solicite ao usuario o nome de um produto, a quantidade comprada e o preço unitário. calcule e exiba o total da compra(ex.:total:r${valor calculado}). aplique um desconto de 5% se o valor total for maior que r$100.

nome_produto = input("insira o nome do produto:")
quantidade = int(input("insira a quantidade comprada:"))
preco_unitario = float(input("insira o preço unitário:"))

total = quantidade * preco_unitario

if total >= 100:
    desconto = 0.05 #desconto de 5%
    valor_com_desconto = total * (1 - desconto)
    print(f"desconto aplicado: 5%")
    print(f"valor final da compra: {valor_com_desconto}")
else:
    print("sem desconto")
    print(f"valor final da compra: {total}")
    