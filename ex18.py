#cálculo de salário com horas extras. crie um programa que: peça o salario base, o numero de horas extras trabalhada e o valor pago por horas extras. calcule o salario total (base + horas extras). exiba o valor total do salario

salario_base = float(input("insira o salario base:"))
horas_extras = int(input("insira o numero de horas extras trabalhadas:"))
valor_hora_extra = float(input("insira o valor pago por horas extras:"))

salario_total = salario_base + (horas_extras * valor_hora_extra)

print(f"salario total: {salario_total}")
