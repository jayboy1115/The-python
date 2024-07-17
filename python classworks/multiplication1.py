for column in range(1, 13):
    print("  ")
    for row in range(1, 11):
        print(f"{column:<2} x {row:<2} = {column * row:^4}",end='  ')
    print()