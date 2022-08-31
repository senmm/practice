def nearest_square(num: int) -> int:
    import math
    if math.sqrt(num) % 1 == 0:
        return num
    for i in range(1,1000000):
        if math.sqrt(num + i) % 1 == 0:
            return (num + i)
        elif math.sqrt(num - i) % 1 == 0:
            return (num - i)
    return 0


print("Example:")
print(nearest_square(8))

assert nearest_square(8) == 9
assert nearest_square(13) == 16

print("The mission is done! Click 'Check Solution' to earn rewards!")
