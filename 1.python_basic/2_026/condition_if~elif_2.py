print('1. 카페라떼(3.5) \t 2. 에스프레소(3.0) \t 3. 아메리카노(2.0) \t 4.곡물라떼(4.0) \t 5. 밀크티(4.3)')
userSelectNumber = int(input('메뉴선택 : '))
print('---------------------')
if userSelectNumber == 1:
    print('메뉴 : 카페라떼')
    print('가격 : 3,500원')
elif userSelectNumber == 2:
    print('메뉴 : 에스프레소')
    print('가격 : 3,000원')
elif userSelectNumber == 3:
    print('메뉴 : 아메리카노')
    print('가격 : 2,000원')
elif userSelectNumber == 4:
    print('메뉴 : 곡물라떼')
    print('가격 : 4,000원')
elif userSelectNumber == 5:
    print('메뉴 : 밀크티')
    print('가격 : 4,300원')
print('---------------------')
