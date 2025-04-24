def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

print("Tasas de ejemplo:")
print("- JPY: 0.0075 (1 JPY = 0.0075 USD)")
print("- MXN: 0.058 (1 MXN = 0.058 USD)")
print("- EUR: 1.05 (1 EUR = 1.05 USD)")


budget = float(input("\nIngresa tu presupuesto en USD: "))
exchange_rate = float(input("Ingresa la tasa de cambio (ej: 0.0075 para JPY): "))

result = exchange_money(budget, exchange_rate)
print(f"\n💵 {budget} USD = {result:.2f} (Moneda extranjera)")