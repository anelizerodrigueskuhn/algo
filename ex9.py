temperatura = float(input("insira a a temperatura"))

if temperatura <= 20:
    print("temperatura frio")
elif temperatura >= 20 and temperatura <= 26:
    print("temperatura normal")
elif temperatura >= 27:
    print("temperatura quente")