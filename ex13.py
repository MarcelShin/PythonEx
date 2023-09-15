vel = int(input("Qual velocidade o carro estava? "))


if vel > 80:
    dif = vel - 80
    multa = dif * 5
    print("Você foi multado no valor de ", multa, "R$")

else:
    print("Parabens você estava a baixo do limite de velocidade =)")

