def second_index(text: str, symbol: str) -> [int, None]:
    first_index = text.find(symbol)
    if first_index < 0:
        return None
    second_index = text.find(symbol,first_index + 1)
    if second_index > first_index:
        return second_index
    return None


print("Example:")
print(second_index("sims", "s"))

assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", " ") == None
assert second_index("hi mayor", " ") == None
assert second_index("hi mr Mayor", " ") == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")
