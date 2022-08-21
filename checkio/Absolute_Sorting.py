def checkio(values: list) -> list:
    temp_list = []
    minus_list = []
    for i in range(len(values)):
        if values[i] < 0:
            minus_list.append(values[i])
        temp_list.append(abs(values[i]))
    temp_list.sort()
    for i in range(len(minus_list)):
        list_index = temp_list.index(abs(minus_list[i]))
        temp_list[list_index] = temp_list[list_index] * -1
    values = temp_list
    return values


if __name__ == '__main__':
    print("Example:")
    print(checkio([-20, -5, 10, 15]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
    assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
    assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
    print("Coding complete? Click 'Check' to earn cool rewards!")
