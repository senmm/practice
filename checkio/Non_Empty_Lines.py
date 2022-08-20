def non_empty_lines(text: str) -> int:
    count = 0
    temp_text = text.split("\n")
    for i in range(len(temp_text)):
        if temp_text[i].replace(" ", "") != "":
            print(temp_text[i].replace(" ", ""))
            count += 1
    return(count)


print("Example:")
print(non_empty_lines("one simple line\n"))

assert non_empty_lines("one simple line\n") == 1
assert non_empty_lines("") == 0
assert non_empty_lines("\nonly one line\n            ") == 1
assert (
    non_empty_lines(
        "\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "
    )
    == 3
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
