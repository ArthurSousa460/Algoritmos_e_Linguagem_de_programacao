a = int(input("digite o valor a da equação: "))
b = int(input("Digite o valor b da equação: "))
c = int(input("Digite o valor c da equação: "))


if a != 0:
    delta = b ** 2 - 4 * a * c
    x1 =  (-b + delta ** (1/2)) / 2 * a
    x2 =  (-b - delta ** (1/2)) / 2 * a

    if delta > 0:
        print(f"O delta é maior que zero, logo terá 2 raizes: {x1} {x2}")
    elif delta == 0:
        print(f"O delta foi igual a zero, logo terá apenas uma raiz: {x1} {x2}")
    else:
        print("O delta deu negativo, não possui raizes!")
else:
    print("a é igual a 0, não há equação.")