def cut_sentence(line: str, length: int) -> str:
    if len(line) > length:
        temp_list = line.split(" ")
        temp_length = 0
        return_string = ""
        for i in range(len(temp_list)):
            temp_length += len(temp_list[i])
            if temp_length <= length:
                return_string = return_string + temp_list[i] + " "
                temp_length += 1
            else:
                return_string = return_string.rstrip() + "..."
                return(return_string)
    # your code here
    return line[:length]


print("Example:")
print(cut_sentence("Hi my name is Alex", 4))

assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"

print("The mission is done! Click 'Check Solution' to earn rewards!")
