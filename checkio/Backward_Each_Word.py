def backward_string_by_word(text: str) -> str:
    temp = text.replace(" ", ",").split(",")
    return_text = ""
    if text == "":
        return("")
    for i in range(len(temp)):
        mojiretsu = str(temp[i])
        if mojiretsu != "":
            if i > 0:
                return_text += " "
            return_text = return_text + mojiretsu[::-1]
        else:
            return_text = return_text + " "
    return(return_text)


print("Example:")
print(backward_string_by_word("hello world"))

assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

print("The mission is done! Click 'Check Solution' to earn rewards!")
