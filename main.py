def dec_to_bin(n):
    return bin(n)[2:]  # bin() funksiyasi bilan ''10-likdan 2-likka o‘tkazish''

# Misol
decimal_number = 10
binary_number = dec_to_bin(decimal_number)
print(f"Decimal: {decimal_number} -> Binary: {binary_number}")
