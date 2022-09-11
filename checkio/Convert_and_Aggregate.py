def conv_aggr(data: list[tuple[str, int]]) -> dict[str, int]:
    key = ""
    value = ""
    d_result ={}
    for index in range(len(data)):
        key = data[index][0]
        value = data[index][1]
        temp = d_result.get(key)
        if temp != None and key != "":
            d_result[key] = temp + value
        elif key != "":
            d_result[key] = value
    return ({k: v for k, v in d_result.items() if v != 0})


print("Example:")
print(conv_aggr([("a", 7), ("b", 8), ("a", 10)]))

assert conv_aggr([("a", 7), ("b", 8), ("a", 10)]) == {"a": 17, "b": 8}
assert conv_aggr([]) == {}
assert conv_aggr([("a", 5), ("a", -5)]) == {}
assert conv_aggr([("a", 5), ("a", 5), ("a", 0)]) == {"a": 10}
assert conv_aggr([("a", 5), ("", 15)]) == {"a": 5}

print("The mission is done! Click 'Check Solution' to earn rewards!")