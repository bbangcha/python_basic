limitWeight = 2200
currentWeight = 800
date = 0

while True:
    date += 1
    currentWeight += 70
    if currentWeight >=2200:
        break

print('이유식 중단 날짜 : {}'.format(date))

