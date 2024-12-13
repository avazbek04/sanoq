def dec_to_hex(n):
    return hex(n)[2:].upper()  # hex() funksiyasi bilan 10-likdan 16-likka o‘tkazish

# Misol
decimal_number = 10
hexadecimal_number = dec_to_hex(decimal_number)
print(f"Decimal: {decimal_number} -> Hexadecimal: {hexadecimal_number}")
