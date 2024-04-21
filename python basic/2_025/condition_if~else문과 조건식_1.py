rainPercentage = int(input('비올 확률 : '))
minrainPercentage = 55

print('우산을 챙기세요') if rainPercentage >= minrainPercentage else print('양산을 챙기세요')

if rainPercentage >= minrainPercentage:
    print('우산을 챙기세요')
else:
    print('양산을 챙기세요')
    