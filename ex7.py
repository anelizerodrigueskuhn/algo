num1=float(input("digite o primeiro numero:"))
num2=float(input("digite o segunto numero:"))
operacao=input("digite a operação(+,-,*,/):")

if operacao=="+":
    print(num1+num2)
elif operacao=="-":
    print(num1-num2)
elif operacao=="*":
    print(num1*num2)
elif operacao=="/":
    print(num1/num2)
else:
    print("operação invalida")
