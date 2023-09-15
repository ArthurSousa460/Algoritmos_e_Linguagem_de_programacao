old_price = float(input("Digite o valor antigo:"))

if old_price <= 50:
    new_price = (old_price * 0.05) + old_price
    print(f"Seu novo preço é: {new_price}")
elif old_price > 50 and old_price <= 100:
    new_price = (old_price * 0.1) + old_price
    print(f"Seu novo preço é: {new_price}")
else:
    new_price = (old_price * 0.15) + old_price
    print(f"Seu novo preço é: {new_price}")


