innerTemp = int(input('실내온도 입력 : '))

if innerTemp <= 18:
    print('에어컨 : OFF!!')
elif innerTemp > 18 and innerTemp <= 22:
    print('에어컨 : 매우 약하게')
elif innerTemp > 22 and innerTemp <= 24:
    print('에어컨 : 약')
elif innerTemp > 24 and innerTemp <= 26:
    print('에어컨 : 중')
elif innerTemp > 26 and innerTemp <= 28:
    print('에어컨 : 강')
elif innerTemp <= 28:
    print('에어컨 : 매우 강')
