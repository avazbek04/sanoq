def dec_to_oct(n):
    return oct(n)[2:]  # oct() funksiyasi bilan 10-likdan 8-likka o‘tkazish

# Misol
decimal_number = 10
octal_number = dec_to_oct(decimal_number)
print(f"Decimal: {decimal_number} -> Octal: {octal_number}")
