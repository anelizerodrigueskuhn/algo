#cálculo de médica de notas. faça um programa que: peça ao usuario tres notas. calcule a média aritmetica das notas. informe se o aluno está aprovado (média >= 7), em recuperação (média entre 5 e 7) ou reprovado (< 5).

nota1 = float(input("insira a primeira nota:"))
nota2 = float(input("insira a segunda nota:"))
nota3 = float(input("insira a terceira nota:"))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("aluno aprovado")
elif media >= 5 and media < 7:
    print("aluno em recuperação")
else:
    print("aluno reprovado")
