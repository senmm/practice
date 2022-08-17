def checkio(array: list[int]) -> int:
    sum = 0
    if len(array) == 0:
        return(0)
    for i in range(len(array)):
        if i % 2 == 0:
            sum += array[i]
    sum = sum * array[-1]
    return(sum)

print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
