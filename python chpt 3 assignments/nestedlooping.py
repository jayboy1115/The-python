for row in range(10):
    for column in range(row+1):
        print('*', end='')
    print('   ', end='')

    
    for column in range(10-row):
        print('*', end='')
    print('   ', end='')

    
    for column in range(10-row):
        print(' ', end='')
    for asterik in range(row+1):
        print('*', end='')
    print('   ', end='')

    
    for column in range(row):
        print(' ', end='')
    for asterik in range(10-row):
        print('*', end='')
    print()
