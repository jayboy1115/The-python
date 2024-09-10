def swap_first_two_chars(str1, str2):
    arr1 = list(str1)
    arr2 = list(str2)

    if len(arr1) > 1:
        arr1[0], arr1[1] = arr1[1], arr1[0]
    if len(arr2) > 1:
        arr2[0], arr2[1] = arr2[1], arr2[0]

    return ''.join(arr1) + ' ' + ''.join(arr2)










