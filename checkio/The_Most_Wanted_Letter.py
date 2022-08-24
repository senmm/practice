def checkio(text: str) -> str:
    from collections import Counter
    import re
    temp = "".join(sorted(text.lower()))
    result = re.sub(r"[^a-z]", "", temp)
    mycounter = Counter(result)

    return (max(mycounter, key=mycounter.get))


print("Example:")
print(checkio("AAaooo!!!!"))

assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"
assert checkio("AAaooo!!!!") == "a"
assert checkio("abe") == "a"

print("The mission is done! Click 'Check Solution' to earn rewards!")
