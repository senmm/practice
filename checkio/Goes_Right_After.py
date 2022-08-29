def goes_after(word: str, first: str, second: str) -> bool:
    if first != second:
        first_index = word.find(first)
        second_index = word.find(second)
    else:
        return False
    if first_index < 0 or second_index < 0:
        return False
    if second_index - first_index == 1:
        return True
    return False


print("Example:")
print(goes_after("world", "w", "o"))

assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
