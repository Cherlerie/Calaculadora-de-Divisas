def exchange_money(budget, exchange_rate):
    return budget * exchange_rate

print("Tasas de ejemplo (1 DOP = X moneda extranjera):")
print("- DOP a USD: 0.017 (1 DOP = 0.017 USD)")
print("- DOP a EUR: 0.015 (1 DOP = 0.015 EUR)")
print("- DOP a JPY: 2.41 (1 DOP = 2.41 JPY)")

budget = float(input("\nIngresa tu presupuesto en DOP: "))
exchange_rate = float(input("Ingresa la tasa de cambio: "))

result = exchange_money(budget, exchange_rate)
print(f"\n💵 {budget} DOP = {result:.2f} (Moneda extranjera)")