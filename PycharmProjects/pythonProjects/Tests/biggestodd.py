def biggest_odd(param):
    maximum = 0

    for number in param:
        if int(number) > maximum and int(number) % 2 != 0:
            maximum = int(number)

    return maximum