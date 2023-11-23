for i in range(7):
    for j in range(7):
        print('O' if i == j or i == 6 - j else '.', end = '')
    print()