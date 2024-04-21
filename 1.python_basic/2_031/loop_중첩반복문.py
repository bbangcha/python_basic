for i in range(1, 10):
    for j in range(2, 10):
        result = j * i
        print('{} * {} = {}\t'.format(j, i, result), end='')
    print()