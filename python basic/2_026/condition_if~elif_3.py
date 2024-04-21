carDisplacement = int(input('자동차 배기량 입력 : '))

if carDisplacement < 1000:
    print('세금 : 100,000원')
elif carDisplacement < 2000 and carDisplacement >= 1000:
    print('세금 : 200,000')
elif carDisplacement < 3000 and carDisplacement >= 2000:
    print('세금 : 300,000')
elif carDisplacement < 4000 and carDisplacement >= 3000:
    print('세금 : 400,000')
elif carDisplacement < 5000 and carDisplacement >= 4000:
    print('세금 : 500,000')
elif carDisplacement >= 5000:
    print('세금 : 600,000')
