def checkio(line1: str, line2: str) -> str:
    line1_list = line1.split(",")
    line2_list = line2.split(",")
    output_list = []
    for i in range(len(line2_list)):
        if line2_list[i] in line1_list:
            output_list.append(line2_list[i])
    return (",".join(sorted(output_list)))


print("Example:")
print(checkio("hello,world", "hello,earth"))

assert checkio("hello,world", "hello,earth") == "hello"
assert checkio("one,two,three", "four,five,six") == ""
assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

print("The mission is done! Click 'Check Solution' to earn rewards!")
