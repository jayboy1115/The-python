def get_items(tuple2):
    result = []
    for i, item in enumerate(tuple2):
        if isinstance(item, (list, tuple)):
            for j, value in enumerate(item):
                if value in [20, 25]:
                    result.append((0 if i == 1 else 1, value))
    return tuple(result)

tuple2 = ("orange", [10, 20, 30], (5, 15, 25))
print(get_items(tuple2))

