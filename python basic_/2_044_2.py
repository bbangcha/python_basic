import datetime

today = datetime.datetime.today()

myage = input('나이 입력 : ')
if myage.isdigit():
    afterage = 100 - int(myage)
    myHundred = today.year + afterage

    print('{}년({}년후에) 100살!'.format(myHundred, afterage))

else:
    print('잘못 입력하였습니다')
