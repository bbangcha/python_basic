year = int(input('연도 입력 : '))

if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
    print('{}년 : 윤년!!'.format(year))
else:
    print('{}년 : 평년!!'.format(year))

for year in range(2021, (2021 + 101)):
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        print('{}년 : 윤년!!'.format(year))
    else:
        print('{}년 : 평년!!'.format(year))
