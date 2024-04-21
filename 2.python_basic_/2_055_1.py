import random

rUum = random.randint(1, 1000)
tryCount = 0
gameFlag = True

while gameFlag:
    tryCount += 1
    pNum = int(input('1에서 1,000까지의 정수 입력 : '))

    if rUum == pNum:
        print('빙고')
        gameFlag = False
    else:
        if rUum > pNum:
            print('난수가 크다!')
        else:
            print('난수가 작다!')

print('난수 : {}, 시도 횟수 : {}'.format(rUum, tryCount))
