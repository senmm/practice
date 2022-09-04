def to_camel_case(name: str) -> str:
    l_name = name.split("_")
    return_str = ""
    for i in range(len(l_name)):
        return_str += l_name[i].capitalize()
    name = return_str
    return name


print("Example:")
print(to_camel_case("my_function_name"))

assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
