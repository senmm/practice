from ast import Return


def bigger_price(limit: int, data: list[dict]) -> list[dict]:
    return_data = []
    sorted_data = sorted(data, key=lambda x:x['price'], reverse=True)
    print(sorted_data)
    for i in range(limit):
        return_data.append(sorted_data[i])
    return return_data
    # your code here
    return []


print("Example:")
print(
    bigger_price(
        2,
        [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1},
        ],
    )
)

assert bigger_price(
    2,
    [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1},
    ],
) == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
assert bigger_price(
    1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
) == [{"name": "whiteboard", "price": 170}]

print("The mission is done! Click 'Check Solution' to earn rewards!")
