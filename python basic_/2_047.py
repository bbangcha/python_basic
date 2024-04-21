money = int(input('금액 입력 : '))
rate = float(input('이율 입력 : '))
term = int(input('기간 입력 : '))

targetMoney = money

for i in range(term):
    targetMoney += targetMoney * rate * 0.01        # targetMoney = targetMoney + (targetMoney * rate * 0.01)

targetMoneyformated = format(int(targetMoney),',')

print('-' * 30)
print('이율 : {}%'.format(rate))
print('원금 : {}'.format(format(money, ',')))
print('{}년 후 금액 : {}원'.format(term, targetMoneyformated))
print('-' * 30)