for row in range(10):
    for column in range(row+1):
        print('*', end='')
    print()

for row in range(10, 0, -1):
    for column in range(row):
        print('*', end='')
    print()

print()  

for row in range(10):
    for column in range(10-row):
        print(' ', end='')
    for asterik in range(row+1):
        print('*', end='')
    print()

print()  

for row in range(10, 0, -1):
    for column in range(10-row):
        print(' ', end='')
    for asterik in range(row):
        print('*', end='')
    print()

