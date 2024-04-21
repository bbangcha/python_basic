lowTemperature = int(input('최저 기온 입력 : '))
highTemperature = int(input('최고 기온 입력 : '))

dailyTemperatureRange = int(highTemperature - lowTemperature)

if dailyTemperatureRange >= 11:
    print('일교차 : {}도'.format(dailyTemperatureRange))
    print('감기 조심하세요')
else:
    print('일교차 : {}도'.format(dailyTemperatureRange))
    print('산책하기 좋은 날씨입니다')

