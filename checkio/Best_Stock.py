def best_stock(data: dict) -> str:
    # your code here
    return(max(data, key=data.get))

print("Example:")
print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

assert best_stock({'CAC': 10.0, 'ATX': 390.2, 'WIG': 1.2}) == 'ATX'
assert best_stock({'CAC': 91.1, 'ATX': 1.01, 'TASI': 120.9}) == 'TASI'

print("The mission is done! Click 'Check Solution' to earn rewards!")
