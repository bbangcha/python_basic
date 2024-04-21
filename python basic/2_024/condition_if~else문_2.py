floatNum = float(input('소수 입력 : '))

if floatNum - int(floatNum) >= 0.5:
    print('올림 : {}'.format(int(floatNum) + 1))
else:
    print('내림 : {}'.format(int(floatNum)))
