def remove_min_max(data: set[int], total: int) -> set[int]:
    if len(data) > total * 2:
        for i in range(total):
            min_value = min(data)
            max_value = max(data)
            data.remove(min_value)
            data.remove(max_value)
        return data
    return set()


print("Example:")
print(remove_min_max({4, 5, 6, 7}, 1))

assert remove_min_max({8, 9, 18, 7}, 1) == {8, 9}
assert remove_min_max({8, 9, 7}, 0) == {8, 9, 7}
assert remove_min_max({8, 9, 7}, 2) == set()
assert remove_min_max({1, 2, 7, 8, 9}, 2) == {7}
assert remove_min_max(set(), 1) == set()

print("The first mission is done! Click 'Check' to earn cool rewards!")
