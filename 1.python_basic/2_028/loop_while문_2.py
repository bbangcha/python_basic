gugudanNum = int(input('희망 구구단 입력 : '))

n = 1
while n < 10:
    result = gugudanNum * n
    print('{} * {} = {}'.format(gugudanNum, n, result))
    n += 1