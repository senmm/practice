def is_ascending(items: list[int]) -> bool:
    if len(items) <= 1:
        return(True)
    for i in range(len(items)):
        if i == 0:
            temp = items[i]
        elif temp >= items[i]:
            return(False)
        else:
            temp = items[i]
    return(True)


print("Example:")
print(is_ascending([-5, 10, 99, 123456]))

assert is_ascending([-5, 10, 99, 123456]) == True
assert is_ascending([99]) == True
assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
assert is_ascending([]) == True
assert is_ascending([1, 1, 1, 1]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
