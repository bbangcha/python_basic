highTemperature = 28
lowTemperature = 20

innerTemperature = int(input('실내 온도 : '))

if innerTemperature >= highTemperature:
    print('냉방 작동!')
    print('실내 온도 조정')
if innerTemperature <= lowTemperature:
    print('난방 작동!')
    print('실내 온도 조정')



