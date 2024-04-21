#첫번째
for i in range(1, 6):
    for j in range(i):
        print('*', end='')
    print()
#두번째
for i1 in range(1, 6):
    for i2 in range(6 - i1 - 1):
        print(' ',end='')
    for i3 in range(i1):
        print('*', end='')
    print()
#세번째
for i4 in range(5, 0, -1):
    for j1 in range(i4):
        print('*', end='')
    print()
#네번째
for i5 in range(5, 0, -1):
    for j2 in range(5 - i5):
        print(' ', end='')

    for j2 in range(i5):
        print('*', end='')

    print()

#다섯번째
for i6 in range(1, 10):
    if i6 < 5:
        for j3 in range(i6):
            print('*', end='')
    else:
        for j3 in range(10 - i6):
            print('*', end='')
    print()

#여섯번째
for i7 in range(1, 6):
    for j4 in range(1, 6):
        if j4 == i7:
            print('*', end='')
        else:
            print(' ', end='')
    print()

