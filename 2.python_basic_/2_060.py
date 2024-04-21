gearATCnt = int(input('GearA 톱니수 입력 : '))
gearBTCnt = int(input('GearB 톱니수 입력 : '))

gearA = 0
gearB = 0
leastNum = 0

flag = True
while flag:

    if gearA != 0:
        if gearA != leastNum:
            gearA += gearATCnt
        else:
            flag = False
    else:
        gearA += gearATCnt

    if gearB != 0 and gearB % gearATCnt == 0:
        leastNum = gearB
    else:
        gearB += gearBTCnt

print('최초 만나는 톱니수(최소공배수) : {}톱니'.format(leastNum))
print('gearA 회전수 : {}회전'.format(int(leastNum / gearATCnt)))
print('gearB 회전수 : {}회전'.format(int(leastNum / gearBTCnt)))