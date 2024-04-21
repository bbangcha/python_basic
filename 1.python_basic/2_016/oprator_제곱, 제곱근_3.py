firstMonthMoney = 200
after12Month = ((firstMonthMoney * 0.01) ** 12) *100

print('12개월 후 용돈 : {}'.format(after12Month))

after12Month = int(after12Month)
strresult = format(after12Month, ',')
print(strresult, '원')