# input_list = [1, 2, 3, 4, 5]
def johnson(num):
    output = {}

    for number in num:
        multiples = number ** 3
        output[number] = multiples
    print(output)

input_list = [1, 2, 3, 4, 5]
print(johnson(input_list))


def get_key_cube(numbers):
    return {number: number ** 3 for number in numbers}