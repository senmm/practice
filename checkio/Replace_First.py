from typing import Iterable

def replace_first(items: list) -> Iterable:
    if len(items) <= 1:
        return(items)
    else:
        return(items[1:] + items[:1])


print("Example:")
print(list(replace_first([1, 2, 3, 4])))

assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
